import codecs
import re

filepath = 'GpuPvSetup/MainWindow.xaml.cs'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

if content.startswith(codecs.BOM_UTF8.decode('utf-8')):
    content = content[len(codecs.BOM_UTF8.decode('utf-8')):]

# 1. Update RunPowerShellCommand signature
content = content.replace(
    'private string RunPowerShellCommand(string command)',
    'private string RunPowerShellCommand(string command, IDictionary<string, string>? envVars = null)'
)

# 2. Add EnvironmentVariables injection
search_env = '''            startInfo.ArgumentList.Add("-Command");
            startInfo.ArgumentList.Add(command);

            using (var process = Process.Start(startInfo))'''
replace_env = '''            startInfo.ArgumentList.Add("-Command");
            startInfo.ArgumentList.Add(command);

            if (envVars != null)
            {
                foreach (var kvp in envVars)
                {
                    startInfo.EnvironmentVariables[kvp.Key] = kvp.Value;
                }
            }

            using (var process = Process.Start(startInfo))'''
content = content.replace(search_env, replace_env)

# 3. Fix WMI Injection
search_wmi_script = '''                    string script = $@"
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

                    string driverPath = RunPowerShellCommand(script).Trim();'''
replace_wmi_script = '''                    var gpuEnvVars = new Dictionary<string, string> { { "GPU_NAME", name } };
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

                    string driverPath = RunPowerShellCommand(script, gpuEnvVars).Trim();'''
content = content.replace(search_wmi_script, replace_wmi_script)

# 4. Fix ConfigureGpuPvAsync Injection (vmName)
search_vm_name = '''            // Sanitize vmName to prevent PowerShell script injection when interpolated inside single quotes.
            vmName = vmName.Replace("'", "''");'''
replace_vm_name = '''            var vmEnvVars = new Dictionary<string, string> { { "VM_NAME", vmName } };'''
content = content.replace(search_vm_name, replace_vm_name)

content = content.replace(
    'RunPowerShellCommand($"Get-VM -Name \'{vmName}\' | Select-Object -ExpandProperty State")',
    'RunPowerShellCommand("Get-VM -Name $env:VM_NAME | Select-Object -ExpandProperty State", vmEnvVars)'
)

content = content.replace(
    'RunPowerShellCommand($"Stop-VM -Name \'{vmName}\' -Force")',
    'RunPowerShellCommand("Stop-VM -Name $env:VM_NAME -Force", vmEnvVars)'
)

content = content.replace(
    'RunPowerShellCommand($"Set-VM -Name \'{vmName}\' -GuestControlledCacheTypes $true -LowMemoryMappedIoSpace 3Gb -HighMemoryMappedIoSpace 33Gb")',
    'RunPowerShellCommand("Set-VM -Name $env:VM_NAME -GuestControlledCacheTypes $true -LowMemoryMappedIoSpace 3Gb -HighMemoryMappedIoSpace 33Gb", vmEnvVars)'
)

content = content.replace(
    'RunPowerShellCommand($"Add-VMGpuPartitionAdapter -VMName \'{vmName}\'")',
    'RunPowerShellCommand("Add-VMGpuPartitionAdapter -VMName $env:VM_NAME", vmEnvVars)'
)

content = content.replace(
    'RunPowerShellCommand($"(Get-VMHardDiskDrive -VMName \'{vmName}\').Path")',
    'RunPowerShellCommand("(Get-VMHardDiskDrive -VMName $env:VM_NAME).Path", vmEnvVars)'
)

content = content.replace(
    'RunPowerShellCommand($"Start-VM -Name \'{vmName}\'")',
    'RunPowerShellCommand("Start-VM -Name $env:VM_NAME", vmEnvVars)'
)

# 5. Fix ConfigureGpuPvAsync Injection (vhdxPath)
search_vhdx = '''                // Sanitize vhdxPath for interpolation inside single quotes
                string safeVhdxPath = vhdxPath.Replace("'", "''");

                progress.Report($"Montando VHDX: {vhdxPath}");
                // Mount-VHD y obtención de la letra de la partición de Windows (suele ser la de mayor tamaño)
                string scriptMount = $@"
                    $vhd = Mount-VHD -Path '{safeVhdxPath}' -PassThru
                    $vol = Get-Disk -Number $vhd.DiskNumber | Get-Partition | Get-Volume | Where-Object {{ $_.DriveLetter }} | Sort-Object Size -Descending | Select-Object -First 1
                    $vol.DriveLetter
                ";
                string driveLetter = RunPowerShellCommand(scriptMount).Trim();'''
replace_vhdx = '''                var vhdxEnvVars = new Dictionary<string, string> { { "VHDX_PATH", vhdxPath } };

                progress.Report($"Montando VHDX: {vhdxPath}");
                // Mount-VHD y obtención de la letra de la partición de Windows (suele ser la de mayor tamaño)
                string scriptMount = @"
                    $vhd = Mount-VHD -Path $env:VHDX_PATH -PassThru
                    $vol = Get-Disk -Number $vhd.DiskNumber | Get-Partition | Get-Volume | Where-Object { $_.DriveLetter } | Sort-Object Size -Descending | Select-Object -First 1
                    $vol.DriveLetter
                ";
                string driveLetter = RunPowerShellCommand(scriptMount, vhdxEnvVars).Trim();'''
content = content.replace(search_vhdx, replace_vhdx)

search_dismount = '''                         string safeVhdxPath = vhdxPath.Replace("'", "''");
                         RunPowerShellCommand($"Dismount-VHD -Path '{safeVhdxPath}'");'''
replace_dismount = '''                         var dismountEnvVars = new Dictionary<string, string> { { "VHDX_PATH", vhdxPath } };
                         RunPowerShellCommand("Dismount-VHD -Path $env:VHDX_PATH", dismountEnvVars);'''
content = content.replace(search_dismount, replace_dismount)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch script complete.")
