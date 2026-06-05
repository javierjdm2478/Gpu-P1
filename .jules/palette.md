## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-06-05 - Accessible selectable logs
**Learning:** Using TextBlock with concatenation for streaming logs in WPF prevents text selection by users and degrades performance (O(N^2) memory allocations), making it inaccessible and inefficient.
**Action:** Use TextBox instead of TextBlock for streaming logs. Configure it with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic a TextBlock's appearance, and use `TextBox.AppendText()` for efficient updates while allowing users and screen readers to interact with the content. Ensure `AutomationProperties.Name` and `ToolTip` are set.
