## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-11-20 - TextBlock to TextBox for Logs
**Learning:** Using `TextBlock` for logs prevents text selection and forces inefficient O(N^2) memory allocations via `+=`.
**Action:** Replace log `TextBlock`s with `TextBox` using `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"`. Use `AppendText()` for efficient updates, allowing users to copy logs easily and adding `AutomationProperties.Name` and `ToolTip` for accessibility.
