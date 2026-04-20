## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - Selectable Logging Text
**Learning:** Using `TextBlock.Text +=` for logs creates O(N^2) allocations and makes logs unselectable, hurting both performance and UX, especially for debugging logs where users often need to copy error messages.
**Action:** Use `TextBox` with `AppendText()`, `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` instead of `TextBlock` to mimic the UI while allowing text selection and better accessibility.
