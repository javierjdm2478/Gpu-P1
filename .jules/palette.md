## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-07 - Interactive and Accessible UI Logs
**Learning:** Using `TextBlock` with string concatenation for frequently updated UI logs prevents users from selecting/copying text and causes O(N^2) memory allocations.
**Action:** For large or frequently updated text logs, replace `TextBlock` inside a `ScrollViewer` with a `TextBox` configured as `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"`. Use `AppendText()` to append logs efficiently and ensure `AutomationProperties.Name` and `ToolTip` are set for accessibility.
