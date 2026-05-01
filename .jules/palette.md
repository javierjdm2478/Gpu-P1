## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-01 - WPF Log View UX Improvement
**Learning:** Using TextBlock with string concatenation for frequent log updates causes poor performance and prevents users from selecting or copying the log text.
**Action:** Use TextBox.AppendText() instead of string concatenation. Configure the TextBox to mimic a TextBlock (IsReadOnly="True", Background="Transparent", BorderThickness="0") to preserve visual layout while allowing text selection and improving performance. Always include AutomationProperties.Name and ToolTip for accessibility.
