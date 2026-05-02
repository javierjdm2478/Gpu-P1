## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-02 - Make logs selectable and accessible
**Learning:** Using a TextBlock inside a ScrollViewer for logs prevents users from selecting or copying the text. It's also less performant due to string concatenation, and lacks proper screen reader support for dynamic text blocks.
**Action:** Use a TextBox with IsReadOnly="True", Background="Transparent", and BorderThickness="0" instead. This allows text selection, supports efficient AppendText(), and ensures better accessibility when paired with AutomationProperties.Name and ToolTip.
