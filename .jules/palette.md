## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-16 - Make Log Text Selectable and Accessible
**Learning:** Using a TextBlock inside a ScrollViewer for logs prevents users from selecting and copying text. Additionally, string concatenation (+=) on TextBlock creates O(N^2) memory allocations which can cause UI lag during operations.
**Action:** Replace TextBlock with a TextBox (IsReadOnly="True", Background="Transparent", BorderThickness="0") to allow text selection while maintaining the same appearance, use AppendText() for performance, and add AutomationProperties.Name and ToolTip in Spanish for accessibility.
