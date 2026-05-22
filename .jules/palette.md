## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-22 - Make application logs selectable and accessible
**Learning:** Using TextBlock with string concatenation for application logs creates a poor UX because the text cannot be selected or copied. It also creates a massive amount of string allocations.
**Action:** Use an accessible read-only TextBox with TextBox.AppendText() to mimic a TextBlock but allow users to copy text out, ensuring accessible names and tooltips are present.
