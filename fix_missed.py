import re
with open("GpuPvSetup/MainWindow.xaml.cs", "r") as f:
    content = f.read()

content = content.replace("""string vhdxPath = RunPowerShellCommand($"(Get-VMHardDiskDrive -VMName '{vmName}').Path").Split(new[] { '\\r', '\\n' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.Trim();""", """string vhdxPath = RunPowerShellCommand("(Get-VMHardDiskDrive -VMName $env:VM_NAME).Path", envVars).Split(new[] { '\\r', '\\n' }, StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()?.Trim();""")

with open("GpuPvSetup/MainWindow.xaml.cs", "w") as f:
    f.write(content)
