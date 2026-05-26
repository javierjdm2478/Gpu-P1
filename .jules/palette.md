## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-26 - WPF TextBox Log Memory Allocation Improvements
**Learning:** For WPF UI logging with frequent text updates, using string concatenation `+=` and `Clear()` with a `TextBlock` causes O(N^2) memory allocations and prevents users from copying the text.
**Action:** Use a `TextBox` with `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"` and call `AppendText()` and `Clear()` on it instead. Ensure to include `AutomationProperties.Name` and `ToolTip` for accessibility.
