## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-13 - Replace TextBlock with TextBox for Logging
**Learning:** TextBlock does not support text selection/copying which is poor UX for a log output, and string concatenation (+=) on TextBlock text degrades performance over time.
**Action:** For logs or frequent text updates, use an auto-scrolling read-only TextBox.AppendText() which allows text selection and prevents memory allocation bottlenecks.
