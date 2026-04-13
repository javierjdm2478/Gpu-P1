grep -n -A 15 "private async void ApplyButton_Click" GpuPvSetup/MainWindow.xaml.cs
grep -n -A 10 "private void LogMessage" GpuPvSetup/MainWindow.xaml.cs
cat GpuPvSetup/MainWindow.xaml | grep -n -A 5 -B 5 "LogTextBlock"
