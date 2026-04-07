## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-03-31 - Better Text UX for Logs
**Learning:** Using a TextBlock for logging in WPF prevents text selection, making it hard to copy logs. Also string concatenation `+=` causes memory allocations.
**Action:** Used `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to visually look like a `TextBlock` but allow users to select text. Updated code to use `TextBox.AppendText()`.
