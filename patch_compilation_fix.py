import os

with open('GpuPvSetup/MainWindow.xaml.cs', 'r', encoding='utf-8-sig') as f:
    content = f.read()

search = '''                    // Método 2: Usar PowerShell con WMI para consultar la clave del registro del servicio y extraer el ImagePath o usar pnputil
                    // Este es un enfoque mucho más robusto que no depende del módulo PnpDevice, que puede fallar o estar ausente.
                    var envVars = new Dictionary<string, string> { { "GPU_NAME", name } };'''

replace = '''                    // Método 2: Usar PowerShell con WMI para consultar la clave del registro del servicio y extraer el ImagePath o usar pnputil
                    // Este es un enfoque mucho más robusto que no depende del módulo PnpDevice, que puede fallar o estar ausente.
                    var detectEnvVars = new Dictionary<string, string> { { "GPU_NAME", name } };'''

content = content.replace(search, replace)

search_2 = '''                    string driverPath = RunPowerShellCommand(script, envVars).Trim();'''

replace_2 = '''                    string driverPath = RunPowerShellCommand(script, detectEnvVars).Trim();'''

content = content.replace(search_2, replace_2)


with open('GpuPvSetup/MainWindow.xaml.cs', 'w', encoding='utf-8') as f:
    f.write(content.replace('\\ufeff', ''))
