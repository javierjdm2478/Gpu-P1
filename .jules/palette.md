## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2026-04-27 - Enable text selection for UI logs
**Learning:** Storing application logs in a `TextBlock` makes it impossible for users to select and copy errors or information.
**Action:** For UI logging, always use `TextBox` instead of `TextBlock` configured with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"`. Additionally, use `TextBox.AppendText()` instead of string concatenation to prevent memory allocation issues and UI freezing.
