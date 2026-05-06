## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - Accessible and Performant WPF Logging
**Learning:** Using `TextBlock.Text += ...` for frequent UI logging causes O(N^2) memory allocations and prevents text selection. Also, logs without ARIA labels are invisible to screen readers.
**Action:** Replace `TextBlock` with `<TextBox IsReadOnly="True" Background="Transparent" BorderThickness="0" TextWrapping="Wrap" VerticalScrollBarVisibility="Auto" />` and use `TextBox.AppendText()`. Always add `AutomationProperties.Name` and `ToolTip`.
