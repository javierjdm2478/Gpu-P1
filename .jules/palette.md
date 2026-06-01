## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-01 - Replace TextBlock with TextBox for logs
**Learning:** Using TextBlock with string concatenation for logs causes O(N^2) memory allocations and prevents users from copying the text, which is bad UX for a setup tool.
**Action:** Replace TextBlock with TextBox (IsReadOnly="True", Background="Transparent", BorderThickness="0") and use AppendText() to improve performance and allow log text selection.
