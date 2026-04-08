## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-04-08 - WPF Log Selection UX Enhancement
**Learning:** For WPF UI logging, repeatedly appending strings to a `TextBlock.Text` causes O(N^2) memory allocations and prevents users from selecting or copying the text.
**Action:** Replace log `TextBlock`s with `TextBox`es and use `TextBox.AppendText()`. To maintain the visual appearance of plain text while adding copyability, configure the `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`. Additionally, add `AutomationProperties.Name` and `ToolTip` to maintain accessibility.
