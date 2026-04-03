## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-04-03 - Accessible UI Logging in WPF
**Learning:** TextBlock elements for frequent log updates lack screen reader focus and accessibility attributes.
**Action:** Replace TextBlock with a TextBox using `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` while maintaining visual styling. Add `AutomationProperties.Name` and `ToolTip` to make the log accessible. Also use `AppendText()` to prevent UI thread blocking allocations.
