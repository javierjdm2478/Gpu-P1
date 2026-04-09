## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-19 - Selectable UI Logs
**Learning:** Using `TextBlock` for logs prevents users from selecting and copying text. Additionally, concatenating strings to `TextBlock.Text` is inefficient.
**Action:** Use a readonly `TextBox` with `Background="Transparent"` and `BorderThickness="0"` to visually mimic a `TextBlock` while enabling text selection. Use `AppendText()` to prevent O(N^2) memory allocations. Always include `AutomationProperties.Name` and `ToolTip` for accessibility.
