import sys
with open('GpuPvSetup/MainWindow.xaml.cs', 'r', encoding='utf-8-sig') as f:
    content = f.read()

search1 = """            // Preparamos la UI para el trabajo en segundo plano
            ApplyButton.IsEnabled = false;
            RefreshVmButton.IsEnabled = false;
            VmComboBox.IsEnabled = false;
            ActionProgressBar.IsIndeterminate = true;
            LogTextBlock.Text = "";"""

replace1 = """            // Preparamos la UI para el trabajo en segundo plano
            ApplyButton.IsEnabled = false;
            RefreshVmButton.IsEnabled = false;
            VmComboBox.IsEnabled = false;
            ActionProgressBar.IsIndeterminate = true;
            LogTextBox.Clear();"""

search2 = """        private void LogMessage(string message)
        {
            // Aseguramos que se ejecute en el hilo de la UI
            Dispatcher.Invoke(() =>
            {
                LogTextBlock.Text += $"[{DateTime.Now:HH:mm:ss}] {message}\\n";
                LogScrollViewer.ScrollToEnd();
            });
        }"""

replace2 = """        private void LogMessage(string message)
        {
            // Aseguramos que se ejecute en el hilo de la UI
            Dispatcher.Invoke(() =>
            {
                LogTextBox.AppendText($"[{DateTime.Now:HH:mm:ss}] {message}\\n");
                LogTextBox.ScrollToEnd();
            });
        }"""

if search1 in content and search2 in content:
    content = content.replace(search1, replace1).replace(search2, replace2)
    with open('GpuPvSetup/MainWindow.xaml.cs', 'w', encoding='utf-8-sig') as f:
        f.write(content)
    print("C# updated.")
else:
    if search1 not in content:
        print("C# pattern 1 not found.")
    if search2 not in content:
        print("C# pattern 2 not found.")
