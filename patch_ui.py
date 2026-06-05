import os

with open('GpuPvSetup/MainWindow.xaml', 'r', encoding='utf-8-sig') as f:
    xaml_content = f.read()

old_xaml = """        <!-- Logs -->
        <Border Grid.Row="4" Background="#252525" CornerRadius="8" Padding="10">
            <ScrollViewer x:Name="LogScrollViewer" VerticalScrollBarVisibility="Auto">
                <TextBlock x:Name="LogTextBlock" TextWrapping="Wrap" FontFamily="Consolas" FontSize="12" Foreground="#00FF00"/>
            </ScrollViewer>
        </Border>"""

new_xaml = """        <!-- Logs -->
        <Border Grid.Row="4" Background="#252525" CornerRadius="8" Padding="10">
            <TextBox x:Name="LogTextBox" IsReadOnly="True" Background="Transparent" BorderThickness="0" TextWrapping="Wrap" VerticalScrollBarVisibility="Auto" FontFamily="Consolas" FontSize="12" Foreground="#00FF00" AutomationProperties.Name="Registro de eventos" ToolTip="Muestra el registro de eventos de la operación"/>
        </Border>"""

xaml_content = xaml_content.replace(old_xaml, new_xaml)

with open('GpuPvSetup/MainWindow.xaml', 'w', encoding='utf-8') as f:
    f.write(xaml_content.replace('\ufeff', ''))

with open('GpuPvSetup/MainWindow.xaml.cs', 'r', encoding='utf-8-sig') as f:
    cs_content = f.read()

old_cs1 = """            LogTextBlock.Text = "";"""
new_cs1 = """            LogTextBox.Clear(); // ⚡ Bolt: Clear() is faster and more memory efficient than assigning empty strings"""

old_cs2 = """            Dispatcher.Invoke(() =>
            {
                LogTextBlock.Text += $"[{DateTime.Now:HH:mm:ss}] {message}\\n";
                LogScrollViewer.ScrollToEnd();
            });"""
new_cs2 = """            Dispatcher.Invoke(() =>
            {
                // ⚡ Bolt: AppendText is significantly faster than string concatenation (+=) for large UI logs
                LogTextBox.AppendText($"[{DateTime.Now:HH:mm:ss}] {message}\\n");
                LogTextBox.ScrollToEnd();
            });"""

cs_content = cs_content.replace(old_cs1, new_cs1)
cs_content = cs_content.replace(old_cs2, new_cs2)

with open('GpuPvSetup/MainWindow.xaml.cs', 'w', encoding='utf-8') as f:
    f.write(cs_content.replace('\ufeff', ''))
