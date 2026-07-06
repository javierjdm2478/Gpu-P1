## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2025-07-06 - Replace TextBlock with TextBox for Logging
**Learning:** In WPF, appending to a TextBlock using string concatenation inside a ScrollViewer is inefficient and doesn't allow text selection.
**Action:** Replace TextBlock with TextBox, set `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"`, remove the redundant ScrollViewer, use `.AppendText()` instead of `+=`, and provide a Spanish ToolTip and AutomationProperties.Name for accessibility and a polished look.
