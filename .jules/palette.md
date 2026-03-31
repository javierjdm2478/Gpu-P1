## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-15 - Logging TextBlock Performance and Accessibility
**Learning:** Frequent string concatenation (`+=`) on `TextBlock.Text` for logging causes O(N^2) memory allocations, slowing down the UI thread, and missing ARIA properties reduces accessibility.
**Action:** Replace `TextBlock` used for logging with `TextBox` using `AppendText()`. To maintain a seamless UI, set `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`. Additionally, apply `AutomationProperties.Name` and `ToolTip` to ensure accessibility.
