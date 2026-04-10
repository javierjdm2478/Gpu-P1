## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-03-31 - WPF UI Logging UX/Accessibility Pattern
**Learning:** For continuous UI logging in WPF, concatenating strings to a TextBlock (+=) causes O(N^2) memory allocations and the text cannot be selected/copied by the user (poor UX).
**Action:** Replace LogTextBlock with a TextBox. Set Background="Transparent", BorderThickness="0", and IsReadOnly="True" to maintain the visual appearance while allowing text selection. Use AppendText() for efficiency, and add AutomationProperties.Name and ToolTip for accessibility.
