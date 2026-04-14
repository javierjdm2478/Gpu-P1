## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-04-12 - Selectable Logs in WPF
**Learning:** Users often need to copy errors or success messages from application logs for troubleshooting, but standard `TextBlock` controls do not support text selection, frustrating users.
**Action:** Use a `TextBox` with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` instead of `TextBlock` for logs. This allows text selection/copying (improving UX) and avoids O(N^2) memory issues when using `AppendText()`.
