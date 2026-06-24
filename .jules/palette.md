## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-24 - WPF Selectable Log Text UX
**Learning:** Using a TextBlock for continuous UI logs prevents users from selecting and copying text for debugging, resulting in poor UX and accessibility. Additionally, string concatenation (+=) on TextBlock is highly inefficient for frequent updates.
**Action:** Use a TextBox with IsReadOnly="True", Background="Transparent", BorderThickness="0", TextWrapping="Wrap", and VerticalScrollBarVisibility="Auto" instead of a TextBlock inside a ScrollViewer. Use AppendText() for updates to natively allow text selection/copying. Always ensure AutomationProperties.Name and ToolTip match the existing UI language (e.g., Spanish).
