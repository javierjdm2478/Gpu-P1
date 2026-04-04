## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-24 - Selectable Log Text
**Learning:** Using TextBlock for application logs prevents users from copying error messages. This can be frustrating when dealing with technical issues.
**Action:** Use a read-only, transparently styled TextBox (with AutomationProperties.Name and ToolTip) instead of TextBlock for displaying logs to allow text selection while maintaining visual consistency.
