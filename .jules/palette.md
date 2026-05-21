## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-21 - Replace TextBlock with TextBox for logging
**Learning:** For WPF UI logging, using `TextBox.AppendText()` instead of string concatenation (`+=`) on a `TextBlock` prevents O(N^2) memory allocations and allows users to select/copy log text. Mimicking a `TextBlock` involves setting `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"`.
**Action:** Always use `TextBox.AppendText()` for frequently updated logs and include `AutomationProperties.Name` and `ToolTip` for accessibility.
