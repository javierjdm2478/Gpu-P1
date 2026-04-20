import os

filepath = "GpuPvSetup/MainWindow.xaml.cs"
with open(filepath, "r", encoding="utf-8-sig") as f:
    content = f.read()

# 1. Update RunPowerShellCommand signature
content = content.replace(
    "private string RunPowerShellCommand(string command)",
    "private string RunPowerShellCommand(string command, IDictionary<string, string>? envVars = null)"
)

# 2. Add env vars application in RunPowerShellCommand
old_start = """            startInfo.ArgumentList.Add("-Command");
            startInfo.ArgumentList.Add(command);

            using (var process = Process.Start(startInfo))"""
new_start = """            startInfo.ArgumentList.Add("-Command");
            startInfo.ArgumentList.Add(command);

            if (envVars != null)
            {
                foreach (var kvp in envVars)
                {
                    startInfo.EnvironmentVariables[kvp.Key] = kvp.Value;
                }
            }

            using (var process = Process.Start(startInfo))"""
content = content.replace(old_start, new_start)

# 3. Refactor DetectHostGpuAndDriver
old_script_gpu = r"""                    string script = $@"
                        $ErrorActionPreference = 'SilentlyContinue'
                        $gpu = Get-CimInstance Win32_VideoController | Where-Object {{ $_.Name -like '*{name}*' }} | Select-Object -First 1
                        if ($gpu) {{
                            $pnpId = $gpu.PNPDeviceID
                            # Escapar los caracteres para regex
                            $escapedPnpId = [regex]::Escape($pnpId)
                            # Buscar en pnputil el nombre original del INF (oemXX.inf)
                            $pnpOut = pnputil /enum-devices /instanceid ""$pnpId""
                            $infLine = $pnpOut | Select-String -Pattern 'Published Name:|Nombre publicado:' | Select-Object -First 1
                            if ($infLine) {{
                                $infName = ($infLine -split ':')[1].Trim()
                                if ($infName) {{
                                    $driverStore = 'C:\Windows\System32\DriverStore\FileRepository'
                                    # Buscar la carpeta que contiene el inf publicado
                                    $folders = Get-ChildItem -Path $driverStore -Directory -Filter ""$($infName.Split('.')[0])*""
                                    if ($folders) {{
                                        $folders[0].FullName
                                    }}
                                }}
                            }}
                        }}
                    ";

                    string driverPath = RunPowerShellCommand(script).Trim();"""

new_script_gpu = r"""                    var gpuEnvVars = new Dictionary<string, string> { { "GPU_NAME", name } };
                    string script = @"
                        $ErrorActionPreference = 'SilentlyContinue'
                        $gpu = Get-CimInstance Win32_VideoController | Where-Object { $_.Name -like ""*$env:GPU_NAME*"" } | Select-Object -First 1
                        if ($gpu) {
                            $pnpId = $gpu.PNPDeviceID
                            # Escapar los caracteres para regex
                            $escapedPnpId = [regex]::Escape($pnpId)
                            # Buscar en pnputil el nombre original del INF (oemXX.inf)
                            $pnpOut = pnputil /enum-devices /instanceid ""$pnpId""
                            $infLine = $pnpOut | Select-String -Pattern 'Published Name:|Nombre publicado:' | Select-Object -First 1
                            if ($infLine) {
                                $infName = ($infLine -split ':')[1].Trim()
                                if ($infName) {
                                    $driverStore = 'C:\Windows\System32\DriverStore\FileRepository'
                                    # Buscar la carpeta que contiene el inf publicado
                                    $folders = Get-ChildItem -Path $driverStore -Directory -Filter ""$($infName.Split('.')[0])*""
                                    if ($folders) {
                                        $folders[0].FullName
                                    }
                                }
                            }
                        }
                    ";

                    string driverPath = RunPowerShellCommand(script, gpuEnvVars).Trim();"""
content = content.replace(old_script_gpu, new_script_gpu)

# 4. Refactor ConfigureGpuPvAsync
old_config_start = """        private void ConfigureGpuPvAsync(string vmName, IProgress<string> progress)
        {
            // Sanitize vmName to prevent PowerShell script injection when interpolated inside single quotes.
            vmName = vmName.Replace("'", "''");

            bool wasVmRunning = false;
            string mountPath = string.Empty;"""
new_config_start = """        private void ConfigureGpuPvAsync(string vmName, IProgress<string> progress)
        {
            var envVars = new Dictionary<string, string> { { "VM_NAME", vmName } };
            bool wasVmRunning = false;
            string mountPath = string.Empty;"""
content = content.replace(old_config_start, new_config_start)

# Update RunPowerShellCommand calls in ConfigureGpuPvAsync
content = content.replace(
    """RunPowerShellCommand($"Get-VM -Name '{vmName}' | Select-Object -ExpandProperty State")""",
    """RunPowerShellCommand("Get-VM -Name $env:VM_NAME | Select-Object -ExpandProperty State", envVars)"""
)
content = content.replace(
    """RunPowerShellCommand($"Stop-VM -Name '{vmName}' -Force")""",
    """RunPowerShellCommand("Stop-VM -Name $env:VM_NAME -Force", envVars)"""
)
content = content.replace(
    """RunPowerShellCommand($"Set-VM -Name '{vmName}' -GuestControlledCacheTypes $true -LowMemoryMappedIoSpace 3Gb -HighMemoryMappedIoSpace 33Gb")""",
    """RunPowerShellCommand("Set-VM -Name $env:VM_NAME -GuestControlledCacheTypes $true -LowMemoryMappedIoSpace 3Gb -HighMemoryMappedIoSpace 33Gb", envVars)"""
)
content = content.replace(
    """RunPowerShellCommand($"Add-VMGpuPartitionAdapter -VMName '{vmName}'")""",
    """RunPowerShellCommand("Add-VMGpuPartitionAdapter -VMName $env:VM_NAME", envVars)"""
)
content = content.replace(
    """RunPowerShellCommand($"(Get-VMHardDiskDrive -VMName '{vmName}').Path")""",
    """RunPowerShellCommand("(Get-VMHardDiskDrive -VMName $env:VM_NAME).Path", envVars)"""
)
content = content.replace(
    """RunPowerShellCommand($"Start-VM -Name '{vmName}'")""",
    """RunPowerShellCommand("Start-VM -Name $env:VM_NAME", envVars)"""
)

# 5. Refactor VHDX mount logic
old_vhdx_logic = r"""                // Sanitize vhdxPath for interpolation inside single quotes
                string safeVhdxPath = vhdxPath.Replace("'", "''");

                progress.Report($"Montando VHDX: {vhdxPath}");
                // Mount-VHD y obtención de la letra de la partición de Windows (suele ser la de mayor tamaño)
                string scriptMount = $@"
                    $vhd = Mount-VHD -Path '{safeVhdxPath}' -PassThru
                    $vol = Get-Disk -Number $vhd.DiskNumber | Get-Partition | Get-Volume | Where-Object {{ $_.DriveLetter }} | Sort-Object Size -Descending | Select-Object -First 1
                    $vol.DriveLetter
                ";
                string driveLetter = RunPowerShellCommand(scriptMount).Trim();"""
new_vhdx_logic = r"""                envVars["VHDX_PATH"] = vhdxPath;

                progress.Report($"Montando VHDX: {vhdxPath}");
                // Mount-VHD y obtención de la letra de la partición de Windows (suele ser la de mayor tamaño)
                string scriptMount = @"
                    $vhd = Mount-VHD -Path $env:VHDX_PATH -PassThru
                    $vol = Get-Disk -Number $vhd.DiskNumber | Get-Partition | Get-Volume | Where-Object { $_.DriveLetter } | Sort-Object Size -Descending | Select-Object -First 1
                    $vol.DriveLetter
                ";
                string driveLetter = RunPowerShellCommand(scriptMount, envVars).Trim();"""
content = content.replace(old_vhdx_logic, new_vhdx_logic)

# 6. Refactor Dismount logic
old_dismount_logic = """                    if (!string.IsNullOrEmpty(vhdxPath))
                    {
                         string safeVhdxPath = vhdxPath.Replace("'", "''");
                         RunPowerShellCommand($"Dismount-VHD -Path '{safeVhdxPath}'");
                         progress.Report("VHDX desmontado.");
                    }"""
new_dismount_logic = """                    if (!string.IsNullOrEmpty(vhdxPath))
                    {
                         envVars["VHDX_PATH"] = vhdxPath;
                         RunPowerShellCommand("Dismount-VHD -Path $env:VHDX_PATH", envVars);
                         progress.Report("VHDX desmontado.");
                    }"""
content = content.replace(old_dismount_logic, new_dismount_logic)

with open(filepath, "w", encoding="utf-8-sig") as f:
    f.write(content)
