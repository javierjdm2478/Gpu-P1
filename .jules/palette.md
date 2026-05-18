## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2026-05-18 - Replacing TextBlock with TextBox for UI Logs
**Learning:** Using a `TextBlock` for append-heavy log outputs in WPF causes O(N^2) allocations via string concatenation and prevents users from selecting/copying text, which harms accessibility and UX.
**Action:** Use a read-only `TextBox` with `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"` and update the code to use `AppendText()` to improve performance and text selection.
