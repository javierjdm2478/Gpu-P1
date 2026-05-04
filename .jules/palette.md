## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-12-05 - WPF Log Component UX and Accessibility Improvement
**Learning:** Using a `TextBlock` for frequently updating logs causes O(N^2) string allocations and doesn't easily allow text selection, which is frustrating for users needing to copy error details. It also lacks inherent accessibility properties.
**Action:** For UI logging, always use `TextBox.AppendText()` with `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"`. Include `AutomationProperties.Name` and `ToolTip` for accessibility.
