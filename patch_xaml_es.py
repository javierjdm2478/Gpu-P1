import sys

with open('GpuPvSetup/MainWindow.xaml', 'r', encoding='utf-8-sig') as f:
    content = f.read()

search_str = """        <!-- Logs -->
        <Border Grid.Row="4" Background="#252525" CornerRadius="8" Padding="10">
            <TextBox x:Name="LogTextBlock"
                     IsReadOnly="True"
                     Background="Transparent"
                     BorderThickness="0"
                     TextWrapping="Wrap"
                     VerticalScrollBarVisibility="Auto"
                     FontFamily="Consolas"
                     FontSize="12"
                     Foreground="#00FF00"
                     AutomationProperties.Name="Registro de eventos"
                     ToolTip="Muestra los registros y el progreso detallado de la operación"/>
        </Border>"""

replace_str = """        <!-- Logs -->
        <Border Grid.Row="4" Background="#252525" CornerRadius="8" Padding="10">
            <TextBox x:Name="LogTextBlock"
                     IsReadOnly="True"
                     Background="Transparent"
                     BorderThickness="0"
                     TextWrapping="Wrap"
                     VerticalScrollBarVisibility="Auto"
                     FontFamily="Consolas"
                     FontSize="12"
                     Foreground="#00FF00"
                     AutomationProperties.Name="Registro de eventos"
                     ToolTip="Muestra los registros y el progreso detallado de la operación"/>
        </Border>"""

if search_str not in content:
    print("Search string not found in MainWindow.xaml! (Already correct?)")
else:
    print("XAML is correct")
