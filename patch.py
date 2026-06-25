import sys

with open('GpuPvSetup/MainWindow.xaml.cs', 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Patch 1: RunPowerShellCommand signature
old1 = r'''        private string RunPowerShellCommand(string command)
        {
            var startInfo = new ProcessStartInfo
            {
                FileName = "powershell.exe",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };'''
new1 = r'''        private string RunPowerShellCommand(string command, Dictionary<string, string>? envVars = null)
        {
            var startInfo = new ProcessStartInfo
            {
                FileName = "powershell.exe",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            if (envVars != null)
            {
                foreach (var kvp in envVars)
                {
                    startInfo.Environment[kvp.Key] = kvp.Value;
                }
            }'''
content = content.replace(old1, new1)

# Patch 2: DetectHostGpuAndDriver
old2 = r'''                    // Este es un enfoque mucho más robusto que no depende del módulo PnpDevice, que puede fallar o estar ausente.
                    string script = $@"
                        $ErrorActionPreference = 'SilentlyContinue'
                        $gpu = Get-CimInstance Win32_VideoController | Where-Object {{ $_.Name -like '*{name}*' }} | Select-Object -First 1'''
new2 = r'''                    // Este es un enfoque mucho más robusto que no depende del módulo PnpDevice, que puede fallar o estar ausente.
                    var gpuEnvVars = new Dictionary<string, string> { { "GPU_NAME", name } };
                    string script = $@"
                        $ErrorActionPreference = 'SilentlyContinue'
                        $gpu = Get-CimInstance Win32_VideoController | Where-Object {{ $_.Name -like ""*$env:GPU_NAME*"" }} | Select-Object -First 1'''
content = content.replace(old2, new2)

old2b = r'''                    string driverPath = RunPowerShellCommand(script).Trim();'''
new2b = r'''                    string driverPath = RunPowerShellCommand(script, gpuEnvVars).Trim();'''
content = content.replace(old2b, new2b)

# Patch 3: ConfigureGpuPvAsync top
old3 = r'''        private void ConfigureGpuPvAsync(string vmName, IProgress<string> progress)
        {
            // Sanitize vmName to prevent PowerShell script injection when interpolated inside single quotes.
            vmName = vmName.Replace("'", "''");

            bool wasVmRunning = false;
            string mountPath = string.Empty;

            try
            {
                // 1. Detección de GPU Host
                progress.Report("Paso 1: Detectando GPU del Host y buscando Drivers...");
                var (gpuVendor, driverPath) = DetectHostGpuAndDriver();
                if (string.IsNullOrEmpty(driverPath))
                    throw new Exception("No se pudo localizar el driver de la GPU en el Host.");

                progress.Report($"GPU Detectada: {gpuVendor}");
                progress.Report($"Ruta del Driver: {driverPath}");

                // 2. Gestionar estado de la VM (Apagar si está encendida)
                progress.Report("Paso 2: Comprobando estado de la VM...");
                string vmState = RunPowerShellCommand($"Get-VM -Name '{vmName}' | Select-Object -ExpandProperty State").Trim();

                if (vmState.Equals("Running", StringComparison.OrdinalIgnoreCase))
                {
                    wasVmRunning = true;
                    progress.Report($"La VM '{vmName}' está encendida. Apagando suavemente...");
                    RunPowerShellCommand($"Stop-VM -Name '{vmName}' -Force");
                    progress.Report("VM apagada.");
                }

                // 3. Configuración MMIO y Adapter
                progress.Report("Paso 3: Configurando MMIO y añadiendo VmgpuPartitionAdapter...");
                RunPowerShellCommand($"Set-VM -Name '{vmName}' -GuestControlledCacheTypes $true -LowMemoryMappedIoSpace 3Gb -HighMemoryMappedIoSpace 33Gb");
                RunPowerShellCommand($"Add-VMGpuPartitionAdapter -VMName '{vmName}'");

                // 4. Montar VHDX
                progress.Report("Paso 4: Buscando y montando el disco VHDX...");
                string vhdxPath = RunPowerShellCommand($"(Get-VMHardDiskDrive -VMName '{vmName}').Path").Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.Trim();

                if (string.IsNullOrEmpty(vhdxPath) || !File.Exists(vhdxPath))
                    throw new Exception($"No se encontró un archivo VHDX válido para la VM en la ruta: {vhdxPath}");

                // Sanitize vhdxPath for interpolation inside single quotes
                string safeVhdxPath = vhdxPath.Replace("'", "''");

                progress.Report($"Montando VHDX: {vhdxPath}");
                // Mount-VHD y obtención de la letra de la partición de Windows (suele ser la de mayor tamaño)
                string scriptMount = $@"
                    $vhd = Mount-VHD -Path '{safeVhdxPath}' -PassThru
                    $vol = Get-Disk -Number $vhd.DiskNumber | Get-Partition | Get-Volume | Where-Object {{ $_.DriveLetter }} | Sort-Object Size -Descending | Select-Object -First 1
                    $vol.DriveLetter
                ";
                string driveLetter = RunPowerShellCommand(scriptMount).Trim();'''
new3 = r'''        private void ConfigureGpuPvAsync(string vmName, IProgress<string> progress)
        {
            var envVars = new Dictionary<string, string> { { "VM_NAME", vmName } };

            bool wasVmRunning = false;
            string mountPath = string.Empty;

            try
            {
                // 1. Detección de GPU Host
                progress.Report("Paso 1: Detectando GPU del Host y buscando Drivers...");
                var (gpuVendor, driverPath) = DetectHostGpuAndDriver();
                if (string.IsNullOrEmpty(driverPath))
                    throw new Exception("No se pudo localizar el driver de la GPU en el Host.");

                progress.Report($"GPU Detectada: {gpuVendor}");
                progress.Report($"Ruta del Driver: {driverPath}");

                // 2. Gestionar estado de la VM (Apagar si está encendida)
                progress.Report("Paso 2: Comprobando estado de la VM...");
                string vmState = RunPowerShellCommand($"Get-VM -Name $env:VM_NAME | Select-Object -ExpandProperty State", envVars).Trim();

                if (vmState.Equals("Running", StringComparison.OrdinalIgnoreCase))
                {
                    wasVmRunning = true;
                    progress.Report($"La VM '{vmName}' está encendida. Apagando suavemente...");
                    RunPowerShellCommand($"Stop-VM -Name $env:VM_NAME -Force", envVars);
                    progress.Report("VM apagada.");
                }

                // 3. Configuración MMIO y Adapter
                progress.Report("Paso 3: Configurando MMIO y añadiendo VmgpuPartitionAdapter...");
                RunPowerShellCommand($"Set-VM -Name $env:VM_NAME -GuestControlledCacheTypes $true -LowMemoryMappedIoSpace 3Gb -HighMemoryMappedIoSpace 33Gb", envVars);
                RunPowerShellCommand($"Add-VMGpuPartitionAdapter -VMName $env:VM_NAME", envVars);

                // 4. Montar VHDX
                progress.Report("Paso 4: Buscando y montando el disco VHDX...");
                string vhdxPath = RunPowerShellCommand($"(Get-VMHardDiskDrive -VMName $env:VM_NAME).Path", envVars).Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.Trim();

                if (string.IsNullOrEmpty(vhdxPath) || !File.Exists(vhdxPath))
                    throw new Exception($"No se encontró un archivo VHDX válido para la VM en la ruta: {vhdxPath}");

                envVars["VHDX_PATH"] = vhdxPath;

                progress.Report($"Montando VHDX: {vhdxPath}");
                // Mount-VHD y obtención de la letra de la partición de Windows (suele ser la de mayor tamaño)
                string scriptMount = $@"
                    $vhd = Mount-VHD -Path $env:VHDX_PATH -PassThru
                    $vol = Get-Disk -Number $vhd.DiskNumber | Get-Partition | Get-Volume | Where-Object {{ $_.DriveLetter }} | Sort-Object Size -Descending | Select-Object -First 1
                    $vol.DriveLetter
                ";
                string driveLetter = RunPowerShellCommand(scriptMount, envVars).Trim();'''
content = content.replace(old3, new3)

# Patch 4: ConfigureGpuPvAsync bottom
old4 = r'''                if (!string.IsNullOrEmpty(mountPath))
                {
                    progress.Report("Desmontando VHDX de forma segura...");
                    string vhdxPath = RunPowerShellCommand($"(Get-VMHardDiskDrive -VMName '{vmName}').Path").Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.Trim();
                    if (!string.IsNullOrEmpty(vhdxPath))
                    {
                         string safeVhdxPath = vhdxPath.Replace("'", "''");
                         RunPowerShellCommand($"Dismount-VHD -Path '{safeVhdxPath}'");
                         progress.Report("VHDX desmontado.");
                    }
                }

                if (wasVmRunning)
                {
                    progress.Report($"Reiniciando la VM '{vmName}' automáticamente...");
                    RunPowerShellCommand($"Start-VM -Name '{vmName}'");
                    progress.Report("VM iniciada.");
                }'''
new4 = r'''                if (!string.IsNullOrEmpty(mountPath))
                {
                    progress.Report("Desmontando VHDX de forma segura...");
                    string cleanVhdxPath = RunPowerShellCommand($"(Get-VMHardDiskDrive -VMName $env:VM_NAME).Path", envVars).Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.Trim();
                    if (!string.IsNullOrEmpty(cleanVhdxPath))
                    {
                         envVars["CLEAN_VHDX_PATH"] = cleanVhdxPath;
                         RunPowerShellCommand($"Dismount-VHD -Path $env:CLEAN_VHDX_PATH", envVars);
                         progress.Report("VHDX desmontado.");
                    }
                }

                if (wasVmRunning)
                {
                    progress.Report($"Reiniciando la VM '{vmName}' automáticamente...");
                    RunPowerShellCommand($"Start-VM -Name $env:VM_NAME", envVars);
                    progress.Report("VM iniciada.");
                }'''
content = content.replace(old4, new4)

# Explicitly remove the \ufeff if present and save
content = content.replace('\ufeff', '')
with open('GpuPvSetup/MainWindow.xaml.cs', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched.")
