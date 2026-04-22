## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2026-04-22 - Selectable and Accessible Logging
**Learning:** Using a TextBlock for frequently updating logs causes O(N^2) memory allocations via string concatenation and prevents users from copying the output.
**Action:** Always use TextBox.AppendText() instead. Make it seamlessly mimic a TextBlock by setting Background="Transparent", BorderThickness="0", IsReadOnly="True", and adding AutomationProperties.Name and ToolTip for accessibility.
