## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-23 - Improve text logging UX and accessibility in WPF
**Learning:** Using a TextBlock within a ScrollViewer for frequent logging is inefficient and unselectable. Users cannot copy logs.
**Action:** Use a TextBox with IsReadOnly="True" and AppendText() to provide better performance and allow users to select/copy logs, ensuring AutomationProperties.Name and ToolTip are set for accessibility.
