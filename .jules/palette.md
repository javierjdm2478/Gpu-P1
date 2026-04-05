## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-03-31 - WPF Logs Selection and Performance
**Learning:** Using `TextBlock.Text +=` for appending logs causes O(N^2) memory allocations, and `TextBlock` prevents users from selecting and copying the log text.
**Action:** Use `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to visually mimic a `TextBlock` while enabling text selection. Use `TextBox.AppendText()` to append logs efficiently. Apply `AutomationProperties.Name` and `ToolTip` to ensure accessibility.
