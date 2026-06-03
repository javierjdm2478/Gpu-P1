import re

with open('GpuPvSetup/MainWindow.xaml', 'r', encoding='utf-8') as f:
    xaml_content = f.read()

with open('GpuPvSetup/MainWindow.xaml.cs', 'r', encoding='utf-8') as f:
    cs_content = f.read()

print("TextBox count in XAML:", xaml_content.count("<TextBox"))
print("TextBlock LogTextBlock uses:", xaml_content.count('x:Name="LogTextBlock"'))

print("LogTextBlock.Text += count in CS:", cs_content.count("LogTextBlock.Text += "))
print("LogTextBlock.Text = count in CS:", cs_content.count('LogTextBlock.Text = ""'))
