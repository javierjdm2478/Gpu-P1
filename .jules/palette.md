## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-18 - Replacing TextBlock with TextBox for Logs in WPF
**Learning:** Using `TextBlock` with string concatenation (`+=`) for frequent log updates causes severe UI thread freezes and excessive memory allocation (O(N^2)). It also lacks basic accessibility and user interaction (text cannot be selected or copied).
**Action:** Always use `TextBox` with `AppendText()` for UI logs. To visually mimic a `TextBlock`, configure `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"`. Include `AutomationProperties.Name` and `ToolTip` to ensure accessibility and explain the new copy capability.
