## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-04-02 - Accessible and Performant UI Logging
**Learning:** For WPF UI logging, `TextBlock.Text += ...` causes UI thread lag and lacks native screen reader support. A read-only, transparent `TextBox` visually matches a `TextBlock` but provides better accessibility and the efficient `AppendText()` method.
**Action:** Replace text block logs with a `TextBox` configured as `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"`. Use `AppendText()` for appending log text, and ensure `AutomationProperties.Name` and `ToolTip` are set.
