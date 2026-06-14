## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-14 - Use TextBox for WPF logs
**Learning:** Using TextBlock with string concatenation for logs causes O(N^2) allocations and is not selectable. TextBox with AppendText is much more efficient and allows copying text.
**Action:** Always use TextBox for WPF logs and frequent text updates.
