## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-23 - TextBox for Logs
**Learning:** TextBlock does not support text selection by the user. When rendering logs, using TextBox with IsReadOnly="True" and AppendText() is preferred for usability and performance without sacrificing the read-only appearance.
**Action:** Always prefer TextBox over TextBlock for UI logs where a user might want to copy/paste text.
