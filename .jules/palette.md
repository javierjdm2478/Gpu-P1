## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2023-10-27 - Improve Log Viewer Performance and Accessibility
**Learning:** Using a `TextBlock` with string concatenation (+=) inside a `ScrollViewer` for continuous logging in WPF causes O(N^2) memory allocations, poor performance, and prevents users from selecting or copying text.
**Action:** Use a read-only `TextBox` with `AppendText()` instead. It handles its own scrolling, avoids memory reallocation, and supports native text selection. Set `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic a `TextBlock` appearance while adding Spanish `AutomationProperties.Name` and `ToolTip` for accessibility.
