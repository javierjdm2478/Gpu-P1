## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-03-31 - WPF Log Viewer Performance and UX
**Learning:** Using `TextBlock.Text += ...` for logs in WPF causes O(N^2) memory allocations and prevents text selection. TextBlock is also poorly read by screen readers in this context.
**Action:** Replace `TextBlock` with `TextBox.AppendText()` for logs. Use `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to mimic the visual style of a TextBlock while allowing users to select/copy text. Add `AutomationProperties.Name` and `ToolTip` for accessibility.
