## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2025-02-14 - Improve WPF Log Selectability and Performance
**Learning:** Using `TextBlock.Text +=` for frequent log updates causes O(N^2) memory allocations and prevents users from selecting/copying text.
**Action:** Use `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to mimic `TextBlock` visually while allowing selection, and use `AppendText()` to improve performance. Add `AutomationProperties.Name` and `ToolTip` for accessibility.
