## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-20 - Selectable Logs in WPF UI
**Learning:** For WPF UI logging, using a `TextBlock` and string concatenation (`+=`) prevents users from selecting or copying the log text, which is a major UX regression for debugging.
**Action:** Use a `TextBox` with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic a `TextBlock` visually while allowing text selection. Use `AppendText()` to avoid O(N^2) memory allocations.
