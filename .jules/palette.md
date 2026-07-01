## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-07-01 - Replace TextBlock with TextBox for WPF UI Logging
**Learning:** For WPF UI logging and frequent text updates, using TextBox.AppendText() is more efficient than string concatenation with TextBlock, and it natively supports selecting/copying text which improves usability.
**Action:** Use TextBox instead of TextBlock with ScrollViewer for logs and mimic TextBlock behavior by setting IsReadOnly="True", Background="Transparent", BorderThickness="0", TextWrapping="Wrap", and VerticalScrollBarVisibility="Auto". Remove any redundant surrounding ScrollViewer.
