## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-26 - Mejorar componente de registro (Log View)
**Learning:** For WPF UI logging and frequent text updates, using TextBlock with string concatenation (+=) and an external ScrollViewer causes O(N^2) memory allocations and prevents users from selecting or copying the text.
**Action:** Replace TextBlock with TextBox. Use TextBox.AppendText() and TextBox.Clear(), set IsReadOnly="True", Background="Transparent", BorderThickness="0", TextWrapping="Wrap", and VerticalScrollBarVisibility="Auto". This mimics TextBlock while enabling text selection and native scrolling. Always include Spanish AutomationProperties.Name and ToolTip for accessibility.
