import re

with open("GpuPvSetup/MainWindow.xaml.cs", "r") as f:
    content = f.read()

print("RunPowerShellCommand calls:")
for line in content.split('\n'):
    if "RunPowerShellCommand(" in line:
        print(line.strip())
