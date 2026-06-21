## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - Improve log viewing and accessibility
**Learning:** In WPF, using `TextBlock` with string concatenation for logs causes memory overhead and prevents text selection. Using a read-only `TextBox` mimicking `TextBlock` allows native scrolling, selection, and better memory management.
**Action:** Replace `TextBlock` with `TextBox` for logs and use `AppendText` and `Clear` methods.
