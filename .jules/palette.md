## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-13 - Make Application Logs Selectable
**Learning:** Using a TextBlock inside a ScrollViewer for application logs prevents users from selecting and copying the text, leading to a frustrating UX.
**Action:** Replace TextBlock + ScrollViewer combinations used for logging with a TextBox configured to look like a TextBlock (IsReadOnly="True", Background="Transparent", BorderThickness="0", TextWrapping="Wrap", VerticalScrollBarVisibility="Auto"). This enables text selection while maintaining the desired visual appearance and native auto-scrolling capabilities.
