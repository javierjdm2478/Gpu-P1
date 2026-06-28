## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-28 - Replace TextBlock with TextBox for Logging
**Learning:** For WPF UI logging and frequent text updates, using TextBox.AppendText() and TextBox.Clear() is more efficient than string concatenation (+=) with TextBlock and provides a better UX by allowing users to select and copy text.
**Action:** When implementing logs or areas with frequent text updates in WPF, use TextBox configured to mimic a TextBlock (IsReadOnly="True", Background="Transparent", BorderThickness="0", TextWrapping="Wrap") rather than a TextBlock inside a ScrollViewer.
