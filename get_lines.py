import sys

with open('GpuPvSetup/MainWindow.xaml.cs', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'RunPowerShellCommand' in line:
        print(f"{i}: {line.strip()}")
