## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2025-02-18 - Replacing TextBlock with TextBox for Logging
**Learning:** For WPF UI logging and frequent text updates, using `TextBox` with `IsReadOnly="True"` instead of `TextBlock` and `ScrollViewer` allows users to select and copy log text natively. It also prevents O(N^2) memory allocations when using `AppendText()`.
**Action:** Always prefer `TextBox` over `TextBlock` for log viewer components, ensuring accessibility properties like `AutomationProperties.Name` and `ToolTip` are set in the application's native language.
