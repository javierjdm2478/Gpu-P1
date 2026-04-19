## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-06-12 - Selectable Logs in WPF
**Learning:** TextBlock for logs prevents users from selecting and copying text (bad for error reporting) and scales poorly with memory allocations via string concatenation.
**Action:** Replace LogTextBlock with a TextBox (IsReadOnly="True", Background="Transparent", BorderThickness="0") and use `.AppendText()`. This provides seamless visual integration while enabling text selection, improving performance, and adding accessibility via AutomationProperties.Name.
