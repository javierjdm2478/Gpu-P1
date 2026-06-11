## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2025-02-12 - Replaced TextBlock with TextBox for logging
**Learning:** Using `TextBlock.Text +=` in WPF creates O(N^2) memory allocations and prevents text selection. Users need to be able to scroll efficiently and copy logs.
**Action:** Always use `TextBox` with `IsReadOnly="True"`, `BorderThickness="0"`, and `Background="Transparent"` for logging components and append text using `AppendText()`.
