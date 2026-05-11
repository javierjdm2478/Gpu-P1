## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-11 - WPF Text Selection and Performance Improvements
**Learning:** Using a `TextBlock` for logs prevents text selection/copying by users and using string concatenation (`+=`) for frequent text updates causes O(N^2) memory allocations.
**Action:** Replace `TextBlock` with `TextBox` (`IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`) to allow selection, and use `.AppendText()` instead of string concatenation to improve performance and avoid memory bloat. Always include `AutomationProperties.Name` and `ToolTip` for accessibility.
