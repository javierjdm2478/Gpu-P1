## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - Make Logs Selectable and Accessible
**Learning:** TextBlock does not support text selection natively, limiting UX for users trying to copy logs. Large string concatenations to TextBlock.Text also cause performance hits.
**Action:** Use an IsReadOnly TextBox instead of a TextBlock to allow copying, style it with Transparent background/0 border to mimic TextBlock, and use `.AppendText()` for performance. Always add AutomationProperties.Name and ToolTip for screen readers.
