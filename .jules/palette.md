## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-06-04 - Mejorar accesibilidad y rendimiento de logs
**Learning:** TextBlock in ScrollViewer for continuous logging causes accessibility issues (screen readers don't handle it well) and poor UX (text is not selectable). String concatenation also leads to high memory usage.
**Action:** Replace ScrollViewer + TextBlock with a single read-only TextBox. Use TextBox.AppendText() and TextBox.ScrollToEnd() for better performance, and include AutomationProperties.Name and ToolTip for accessibility.
