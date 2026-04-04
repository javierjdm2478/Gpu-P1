import re
with open("GpuPvSetup/MainWindow.xaml.cs", "r") as f:
    content = f.read()

# Replace vmName sanitization and usage
content = content.replace("""        private void ConfigureGpuPvAsync(string vmName, IProgress<string> progress)
        {
            // Sanitize vmName to prevent PowerShell script injection when interpolated inside single quotes.
            vmName = vmName.Replace("'", "''");""", """        private void ConfigureGpuPvAsync(string vmName, IProgress<string> progress)
        {
            var envVars = new Dictionary<string, string> { { "VM_NAME", vmName } };""")

content = content.replace("""string vmState = RunPowerShellCommand($"Get-VM -Name '{vmName}' | Select-Object -ExpandProperty State").Trim();""", """string vmState = RunPowerShellCommand("Get-VM -Name $env:VM_NAME | Select-Object -ExpandProperty State", envVars).Trim();""")

content = content.replace("""RunPowerShellCommand($"Stop-VM -Name '{vmName}' -Force");""", """RunPowerShellCommand("Stop-VM -Name $env:VM_NAME -Force", envVars);""")

content = content.replace("""RunPowerShellCommand($"Set-VM -Name '{vmName}' -GuestControlledCacheTypes $true -LowMemoryMappedIoSpace 3Gb -HighMemoryMappedIoSpace 33Gb");""", """RunPowerShellCommand("Set-VM -Name $env:VM_NAME -GuestControlledCacheTypes $true -LowMemoryMappedIoSpace 3Gb -HighMemoryMappedIoSpace 33Gb", envVars);""")

content = content.replace("""RunPowerShellCommand($"Add-VMGpuPartitionAdapter -VMName '{vmName}'");""", """RunPowerShellCommand("Add-VMGpuPartitionAdapter -VMName $env:VM_NAME", envVars);""")

content = content.replace("""string vhdxPath = RunPowerShellCommand($"(Get-VMHardDiskDrive -VMName '{vmName}').Path").Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.Trim();""", """string vhdxPath = RunPowerShellCommand("(Get-VMHardDiskDrive -VMName $env:VM_NAME).Path", envVars).Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.Trim();""")

# Replace vhdxPath sanitization and usage
content = content.replace("""                // Sanitize vhdxPath for interpolation inside single quotes
                string safeVhdxPath = vhdxPath.Replace("'", "''");

                progress.Report($"Montando VHDX: {vhdxPath}");
                // Mount-VHD y obtención de la letra de la partición de Windows (suele ser la de mayor tamaño)
                string scriptMount = $@"
                    $vhd = Mount-VHD -Path '{safeVhdxPath}' -PassThru
                    $vol = Get-Disk -Number $vhd.DiskNumber | Get-Partition | Get-Volume | Where-Object {{ $_.DriveLetter }} | Sort-Object Size -Descending | Select-Object -First 1
                    $vol.DriveLetter
                ";
                string driveLetter = RunPowerShellCommand(scriptMount).Trim();""", """                envVars["VHDX_PATH"] = vhdxPath;

                progress.Report($"Montando VHDX: {vhdxPath}");
                // Mount-VHD y obtención de la letra de la partición de Windows (suele ser la de mayor tamaño)
                string scriptMount = @"
                    $vhd = Mount-VHD -Path $env:VHDX_PATH -PassThru
                    $vol = Get-Disk -Number $vhd.DiskNumber | Get-Partition | Get-Volume | Where-Object { $_.DriveLetter } | Sort-Object Size -Descending | Select-Object -First 1
                    $vol.DriveLetter
                ";
                string driveLetter = RunPowerShellCommand(scriptMount, envVars).Trim();""")

content = content.replace("""                         string safeVhdxPath = vhdxPath.Replace("'", "''");
                         RunPowerShellCommand($"Dismount-VHD -Path '{safeVhdxPath}'");""", """                         envVars["VHDX_PATH"] = vhdxPath;
                         RunPowerShellCommand("Dismount-VHD -Path $env:VHDX_PATH", envVars);""")

content = content.replace("""RunPowerShellCommand($"Start-VM -Name '{vmName}'");""", """RunPowerShellCommand("Start-VM -Name $env:VM_NAME", envVars);""")

# DetectHostGpuAndDriver
content = content.replace("""                    // Método 2: Usar PowerShell con WMI para consultar la clave del registro del servicio y extraer el ImagePath o usar pnputil
                    // Este es un enfoque mucho más robusto que no depende del módulo PnpDevice, que puede fallar o estar ausente.
                    string script = $@"
                        $ErrorActionPreference = 'SilentlyContinue'
                        $gpu = Get-CimInstance Win32_VideoController | Where-Object {{ $_.Name -like '*{name}*' }} | Select-Object -First 1""", """                    // Método 2: Usar PowerShell con WMI para consultar la clave del registro del servicio y extraer el ImagePath o usar pnputil
                    // Este es un enfoque mucho más robusto que no depende del módulo PnpDevice, que puede fallar o estar ausente.
                    var envVars = new Dictionary<string, string> { { "GPU_NAME", name } };
                    string script = @"
                        $ErrorActionPreference = 'SilentlyContinue'
                        $gpu = Get-CimInstance Win32_VideoController | Where-Object { $_.Name -like '*'+$env:GPU_NAME+'*' } | Select-Object -First 1""")

content = content.replace("""string driverPath = RunPowerShellCommand(script).Trim();""", """string driverPath = RunPowerShellCommand(script, envVars).Trim();""")

with open("GpuPvSetup/MainWindow.xaml.cs", "w") as f:
    f.write(content)
