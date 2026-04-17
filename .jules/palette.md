## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-04-17 - Use TextBox for UI logs instead of TextBlock
**Learning:** Using a TextBlock for continuous logging creates performance issues due to O(N^2) memory allocations when appending strings via `+=`. It also prevents users from copying error messages, which is terrible UX.
**Action:** For UI logs, always use a `TextBox` with `AppendText()`. To maintain a seamless look, apply `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`. Additionally, provide `AutomationProperties.Name` and `ToolTip` for accessibility.
