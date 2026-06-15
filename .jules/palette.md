## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-15 - Replace TextBlock with TextBox for selectable logs
**Learning:** WPF users expect application logs to be selectable and copyable. Using a TextBlock prevents selection. A read-only TextBox styled to look like a TextBlock is the correct UX pattern for logs.
**Action:** Always use TextBox with IsReadOnly="True", Background="Transparent", and BorderThickness="0" instead of TextBlock for any text that a user might need to copy (like logs or error details).
