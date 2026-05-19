## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-19 - Replace TextBlock with TextBox for Logs
**Learning:** For WPF UI logging, using `TextBlock.Text += ...` leads to O(N^2) memory allocations and prevents text selection.
**Action:** Use `TextBox` with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` combined with `AppendText()` for logs. Always include `AutomationProperties.Name` and `ToolTip` for accessibility.
