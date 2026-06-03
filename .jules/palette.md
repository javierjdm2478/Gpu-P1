## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2026-06-03 - Reemplazar TextBlock con TextBox para logs
**Learning:** En WPF, usar `TextBlock` con concatenación de strings para logs frecuentes causa problemas de rendimiento por asignación de memoria O(N^2) y no permite seleccionar el texto.
**Action:** Reemplazar `TextBlock` y `ScrollViewer` por un `TextBox` con `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"` y `VerticalScrollBarVisibility="Auto"` usando `TextBox.AppendText()` y `TextBox.ScrollToEnd()`. Se deben añadir siempre `AutomationProperties.Name` y `ToolTip` (en español en este caso) para la accesibilidad.
