## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-06-25 - WPF Log TextBlock to TextBox Migration
**Learning:** Replaced a WPF `TextBlock` within a `ScrollViewer` with a `TextBox` for UI logging. Utilizing `TextBox.AppendText()` prevents O(N^2) memory allocations from string concatenation and gives users the ability to select/copy the text, enhancing accessibility and performance.
**Action:** Always prefer `TextBox` with `AppendText()` over `TextBlock` string concatenation for frequent log updates. Set `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"` to retain the visual appearance of a plain text block.
