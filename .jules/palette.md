## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-09 - UI Log Performance and Accessibility Enhancement
**Learning:** Using `TextBlock` and string concatenation (`+=`) for frequent UI log updates is a major accessibility and memory antipattern in WPF. The text is not selectable by users, and it allocates memory quadratically.
**Action:** Replace log `TextBlock`s with `TextBox`es that use `.AppendText()`. Style the `TextBox` to look like a standard `TextBlock` by setting `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, and `VerticalScrollBarVisibility="Auto"`. Ensure that `AutomationProperties.Name` and `ToolTip` are set for screen reader accessibility, allowing users to select and read the log.
