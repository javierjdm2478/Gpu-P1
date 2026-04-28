## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2025-01-20 - Selectable Logs in WPF
**Learning:** Using TextBlock for long-running append-only logs causes O(N^2) memory allocations and prevents text selection.
**Action:** Use TextBox with `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"` and `AppendText()` to improve performance and allow the user to select and copy the text. Include `AutomationProperties.Name` and `ToolTip` for accessibility.
