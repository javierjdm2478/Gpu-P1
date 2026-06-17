## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-15 - WPF Logs Selection
**Learning:** Using `TextBlock` for logs prevents text selection.
**Action:** Replace `TextBlock` and surrounding `ScrollViewer` with a `TextBox` configured to mimic `TextBlock` (`IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `VerticalScrollBarVisibility="Auto"`), allowing users to select/copy logs without O(N^2) memory allocations via `.AppendText()`.
