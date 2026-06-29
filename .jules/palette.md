## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - Enable log text selection for better UX
**Learning:** Users often need to copy output paths or error messages from diagnostic logs, which is impossible with a standard `TextBlock`. Additionally, frequent string concatenation (`+=`) on a `TextBlock` causes memory and performance issues, whereas `TextBox.AppendText()` is optimized for this.
**Action:** Use a readonly, transparent `TextBox` with `AppendText()` instead of a `TextBlock` for logs. Ensure `AutomationProperties.Name` and `ToolTip` are included for accessibility.
