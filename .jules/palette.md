## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-24 - Make WPF event logs selectable and accessible
**Learning:** Using TextBlock for frequent text updates and logs is non-selectable, which hurts UX. Concatenating strings to TextBlock.Text also causes O(N^2) memory allocations.
**Action:** Replace TextBlock logs with a TextBox with AppendText(). To visually mimic a TextBlock seamlessly, set Background="Transparent", BorderThickness="0", and IsReadOnly="True" on the TextBox, and apply AutomationProperties.Name and ToolTip for screen reader accessibility.
