## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-04-01 - Accessible and Performant UI Logging
**Learning:** Using a `TextBlock` for frequent text updates causes O(N^2) memory allocations and lacks screen reader accessibility out-of-the-box.
**Action:** Use a `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to visually mimic a `TextBlock`. Use `.AppendText()` for updates, and apply `AutomationProperties.Name` and `ToolTip` to ensure accessibility for screen readers.
