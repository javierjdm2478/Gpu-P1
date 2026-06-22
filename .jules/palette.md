## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-03-31 - WPF Logs Copyability and Performance
**Learning:** TextBlocks in WPF do not allow text selection out-of-the-box, making them poor choices for displaying error logs where users need to copy details. String concatenation on TextBlocks is also a memory/performance drag.
**Action:** Use a read-only TextBox with `Background="Transparent"` and `BorderThickness="0"` instead of a TextBlock to mimic text while allowing copy-paste. Use `TextBox.AppendText()` for appending logs efficiently and leverage its built-in scrollbar visibility instead of a separate ScrollViewer.
