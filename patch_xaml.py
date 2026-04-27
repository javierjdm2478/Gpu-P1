import sys
with open('GpuPvSetup/MainWindow.xaml', 'r', encoding='utf-8-sig') as f:
    content = f.read()

search = """        <!-- Logs -->
        <Border Grid.Row="4" Background="#252525" CornerRadius="8" Padding="10">
            <ScrollViewer x:Name="LogScrollViewer" VerticalScrollBarVisibility="Auto">
                <TextBlock x:Name="LogTextBlock" TextWrapping="Wrap" FontFamily="Consolas" FontSize="12" Foreground="#00FF00"/>
            </ScrollViewer>
        </Border>"""

replace = """        <!-- Logs -->
        <Border Grid.Row="4" Background="#252525" CornerRadius="8" Padding="10">
            <TextBox x:Name="LogTextBox" TextWrapping="Wrap" FontFamily="Consolas" FontSize="12" Foreground="#00FF00" IsReadOnly="True" Background="Transparent" BorderThickness="0" VerticalScrollBarVisibility="Auto" AutomationProperties.Name="Registro de actividad" ToolTip="Registro detallado de las operaciones de la aplicación. Puede seleccionar y copiar el texto."/>
        </Border>"""

if search in content:
    with open('GpuPvSetup/MainWindow.xaml', 'w', encoding='utf-8-sig') as f:
        f.write(content.replace(search, replace))
    print("XAML updated.")
else:
    print("XAML pattern not found.")
