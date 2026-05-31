## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-31 - WPF Selectable Logs
**Learning:** TextBlock for logs prevents users from selecting or copying text. Appending text to TextBlock also creates O(N^2) allocations.
**Action:** Use a readonly TextBox instead of TextBlock for logs. It natively supports selection, copying, and efficient appending (AppendText), and handles its own scrolling.
