## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-03-31 - Log viewer accessibility
**Learning:** TextBlock log viewers do not support text selection natively and offer poor support for screen reading and scrolling accessibility.
**Action:** Replace `TextBlock` with `TextBox` configured with IsReadOnly="True", Background="Transparent", and BorderThickness="0" for log viewers to support native scroll, selection, and ARIA properties.
