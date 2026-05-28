## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-18 - Replacing WPF TextBlock with TextBox for Accessible Log Viewing
**Learning:** TextBlock elements used for logs in WPF cannot be highlighted or copied by the user and are not inherently accessible. Additionally, repeatedly appending to a TextBlock using string concatenation causes significant memory allocation and performance degradation over time.
**Action:** Use a `TextBox` with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to visually mimic a TextBlock while natively supporting text selection, copying, and scrolling (`ScrollToEnd()`). Use `TextBox.AppendText()` instead of string concatenation to optimize memory usage, and add `AutomationProperties.Name` with a `ToolTip` to ensure screen reader accessibility.
