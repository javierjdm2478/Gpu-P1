using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Management;
using System.Threading.Tasks;
using System.Windows;

namespace GpuPvSetup
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            LoadVirtualMachines();
        }

        private async void RefreshVmButton_Click(object sender, RoutedEventArgs e)
        {
            await LoadVirtualMachines();
        }

        private async Task LoadVirtualMachines()
        {
            VmComboBox.Items.Clear();
            RefreshVmButton.IsEnabled = false;
            LogMessage("Cargando lista de Máquinas Virtuales...");

            try
            {
                // Obtenemos las VMs de Hyper-V mediante PowerShell de manera asíncrona
                var vms = await Task.Run(() => RunPowerShellCommand("Get-VM | Select-Object -ExpandProperty Name"));
                var vmList = vms.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries).ToList();

                foreach (var vm in vmList)
                {
                    VmComboBox.Items.Add(vm);
                }

                if (VmComboBox.Items.Count > 0)
                {
                    VmComboBox.SelectedIndex = 0;
                    LogMessage($"Se encontraron {VmComboBox.Items.Count} máquinas virtuales.");
                }
                else
                {
                    LogMessage("No se encontraron máquinas virtuales en Hyper-V.");
                }
            }
            catch (Exception ex)
            {
                LogMessage($"Error al cargar VMs: {ex.Message}");
            }
            finally
            {
                RefreshVmButton.IsEnabled = true;
            }
        }

        private async void ApplyButton_Click(object sender, RoutedEventArgs e)
        {
            if (VmComboBox.SelectedItem == null)
            {
                MessageBox.Show("Por favor, seleccione una máquina virtual primero.", "Atención", MessageBoxButton.OK, MessageBoxImage.Warning);
                return;
            }

            string selectedVm = VmComboBox.SelectedItem.ToString() ?? string.Empty;

            // Preparamos la UI para el trabajo en segundo plano
            ApplyButton.IsEnabled = false;
            RefreshVmButton.IsEnabled = false;
            VmComboBox.IsEnabled = false;
            ActionProgressBar.IsIndeterminate = true;
            LogTextBox.Clear();

            // Creamos un objeto para reportar el progreso desde el hilo secundario
            var progress = new Progress<string>(message =>
            {
                StatusTextBlock.Text = message;
                LogMessage(message);
            });

            try
            {
                // Ejecutamos todo el proceso pesado en un hilo secundario
                await Task.Run(() => ConfigureGpuPvAsync(selectedVm, progress));
                MessageBox.Show("¡Configuración GPU-PV completada con éxito!", "Éxito", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            catch (Exception ex)
            {
                LogMessage($"ERROR CRÍTICO: {ex.Message}");
                MessageBox.Show($"Ocurrió un error:\n{ex.Message}", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }
            finally
            {
                // Restauramos la UI
                ApplyButton.IsEnabled = true;
                RefreshVmButton.IsEnabled = true;
                VmComboBox.IsEnabled = true;
                ActionProgressBar.IsIndeterminate = false;
                StatusTextBlock.Text = "Listo.";
            }
        }

        private void ConfigureGpuPvAsync(string vmName, IProgress<string> progress)
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
                string driveLetter = RunPowerShellCommand(scriptMount).Trim();

                if (string.IsNullOrEmpty(driveLetter))
                    throw new Exception("No se pudo obtener la letra de la unidad montada del VHDX.");

                mountPath = $"{driveLetter}:\\";
                progress.Report($"VHDX montado en la unidad {mountPath}");

                // 5. Copia de archivos del driver
                progress.Report("Paso 5: Copiando archivos de driver a la VM...");
                string vmDriverStorePath = Path.Combine(mountPath, @"Windows\System32\HostDriverStore\FileRepository");
                string destDriverFolder = Path.Combine(vmDriverStorePath, new DirectoryInfo(driverPath).Name);

                if (!Directory.Exists(vmDriverStorePath))
                {
                    Directory.CreateDirectory(vmDriverStorePath);
                }

                CopyDirectory(driverPath, destDriverFolder, progress);

                // Lógica condicional: NVIDIA nvapi64.dll
                if (gpuVendor.Contains("NVIDIA", StringComparison.OrdinalIgnoreCase))
                {
                    progress.Report("NVIDIA detectada: Copiando nvapi64.dll al System32 de la VM...");
                    string nvapiHostPath = Path.Combine(Environment.SystemDirectory, "nvapi64.dll");
                    string nvapiVmPath = Path.Combine(mountPath, @"Windows\System32\nvapi64.dll");

                    if (File.Exists(nvapiHostPath))
                    {
                        File.Copy(nvapiHostPath, nvapiVmPath, true);
                        progress.Report("nvapi64.dll copiado correctamente.");
                    }
                    else
                    {
                        progress.Report("ADVERTENCIA: No se encontró nvapi64.dll en el Host System32.");
                    }
                }

                progress.Report("Proceso principal finalizado correctamente.");
            }
            finally
            {
                // 6. Restauración: Desmontar VHDX y reiniciar si es necesario
                progress.Report("Paso 6: Limpieza y Restauración...");

                if (!string.IsNullOrEmpty(mountPath))
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
                }

                progress.Report("Operación terminada.");
            }
        }

        private (string Vendor, string DriverPath) DetectHostGpuAndDriver()
        {
            // Usamos WMI para buscar el controlador de video
            using (var searcher = new ManagementObjectSearcher("SELECT * FROM Win32_VideoController"))
            {
                foreach (ManagementObject obj in searcher.Get())
                {
                    string name = obj["Name"]?.ToString() ?? string.Empty;

                    // Ignorar adaptadores básicos o remotos
                    if (name.Contains("Microsoft Basic", StringComparison.OrdinalIgnoreCase) ||
                        name.Contains("Remote", StringComparison.OrdinalIgnoreCase))
                        continue;

                    // Método 1: Intentar leer 'InstalledDisplayDrivers' (Suele funcionar bien para AMD e Intel, y a veces NVIDIA)
                    string installedDrivers = obj["InstalledDisplayDrivers"]?.ToString() ?? string.Empty;
                    if (!string.IsNullOrEmpty(installedDrivers))
                    {
                        var paths = installedDrivers.Split(',');
                        foreach (var path in paths)
                        {
                            if (path.Contains(@"DriverStore\FileRepository", StringComparison.OrdinalIgnoreCase))
                            {
                                string dir = Path.GetDirectoryName(path);
                                if (!string.IsNullOrEmpty(dir) && Directory.Exists(dir))
                                {
                                    return (name, dir);
                                }
                            }
                        }
                    }

                    // Método 2: Usar PowerShell con WMI para consultar la clave del registro del servicio y extraer el ImagePath o usar pnputil
                    // Este es un enfoque mucho más robusto que no depende del módulo PnpDevice, que puede fallar o estar ausente.
                    string script = $@"
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

                    string driverPath = RunPowerShellCommand(script).Trim();

                    if (!string.IsNullOrEmpty(driverPath) && Directory.Exists(driverPath))
                    {
                        return (name, driverPath);
                    }
                }
            }
            return ("Unknown", string.Empty);
        }

        private void CopyDirectory(string sourceDir, string destinationDir, IProgress<string> progress, Stopwatch? stopwatch = null)
        {
            if (stopwatch == null)
            {
                stopwatch = Stopwatch.StartNew();
            }

            var dir = new DirectoryInfo(sourceDir);

            if (!dir.Exists)
                throw new DirectoryNotFoundException($"Source directory not found: {dir.FullName}");

            DirectoryInfo[] dirs = dir.GetDirectories();
            Directory.CreateDirectory(destinationDir);

            FileInfo[] files = dir.GetFiles();
            int totalFiles = files.Length;
            int count = 0;

            foreach (FileInfo file in files)
            {
                string targetFilePath = Path.Combine(destinationDir, file.Name);
                file.CopyTo(targetFilePath, true);
                count++;

                // ⚡ Bolt: Throttling IProgress<string>.Report calls to reduce UI thread context switches
                if (stopwatch.ElapsedMilliseconds > 100 || count == totalFiles)
                {
                     progress.Report($"Copiando archivos del driver... ({count}/{totalFiles})");
                     stopwatch.Restart();
                }
            }

            foreach (DirectoryInfo subDir in dirs)
            {
                string newDestinationDir = Path.Combine(destinationDir, subDir.Name);
                CopyDirectory(subDir.FullName, newDestinationDir, progress, stopwatch); // No mostramos sub-progreso para simplificar
            }
        }

        private string RunPowerShellCommand(string command)
        {
            var startInfo = new ProcessStartInfo
            {
                FileName = "powershell.exe",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            startInfo.ArgumentList.Add("-NoProfile");
            startInfo.ArgumentList.Add("-ExecutionPolicy");
            startInfo.ArgumentList.Add("Bypass");
            startInfo.ArgumentList.Add("-Command");
            startInfo.ArgumentList.Add(command);

            using (var process = Process.Start(startInfo))
            {
                if (process == null) return string.Empty;
                string output = process.StandardOutput.ReadToEnd();
                string error = process.StandardError.ReadToEnd();
                process.WaitForExit();

                if (!string.IsNullOrEmpty(error))
                {
                    // Algunos comandos PS envían advertencias a StdErr, si es fatal, deberíamos controlarlo.
                    // Aquí lo registramos en consola de debug.
                    Debug.WriteLine($"PS Error: {error}");
                }

                return output;
            }
        }

        private void LogMessage(string message)
        {
            // Aseguramos que se ejecute en el hilo de la UI
            Dispatcher.Invoke(() =>
            {
                // ⚡ Bolt: Usando AppendText en TextBox para evitar asignaciones de memoria O(N^2)
                LogTextBox.AppendText($"[{DateTime.Now:HH:mm:ss}] {message}\n");
                LogTextBox.ScrollToEnd();
            });
        }
    }
}
