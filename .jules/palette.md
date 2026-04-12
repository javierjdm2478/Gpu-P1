## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-24 - Selectable logs for better UX
**Learning:** Using a `TextBlock` for application logs prevents users from selecting and copying text (e.g., error messages), resulting in poor UX. Appending to a `TextBlock.Text` also incurs O(N^2) memory allocations.
**Action:** Use a `TextBox` configured to visually match a `TextBlock` (`Background="Transparent"`, `BorderThickness="0"`, `IsReadOnly="True"`) with `AutomationProperties.Name` and `ToolTip` for accessibility. Update text using `TextBox.AppendText()` instead of string concatenation.
