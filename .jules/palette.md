## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-12 - Improve log viewer accessibility and usability
**Learning:** Using a TextBlock for continuous log output causes poor performance due to string concatenation (O(N^2) memory allocations) and prevents users from selecting or copying the log text.
**Action:** Replace TextBlock wrapped in ScrollViewer with a read-only TextBox (IsReadOnly="True", Background="Transparent", BorderThickness="0"). This enables text selection, improves performance via AppendText(), and allows native scrolling while maintaining the same visual appearance. Always add AutomationProperties.Name and ToolTip for accessibility.
