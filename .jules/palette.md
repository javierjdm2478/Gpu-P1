## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-18 - Replacing string concatenation with TextBox AppendText for logs
**Learning:** Frequent UI logging updates using string concatenation (`+=`) in a WPF `TextBlock` causes O(N^2) memory allocations and prevents users from selecting or copying the text.
**Action:** Replace `TextBlock` with a `TextBox` configured to mimic a `TextBlock` (`IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, `VerticalScrollBarVisibility="Auto"`). Update the C# backend to use `TextBox.AppendText()` instead of `+=` to improve performance and allow text selection. Always include `AutomationProperties.Name` and `ToolTip` for accessibility.
