## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2025-02-18 - Replacing WPF TextBlock with TextBox for selectable logs
**Learning:** Using a TextBlock with string concatenation for logs causes O(N^2) memory allocations and poor accessibility, as users cannot select or copy the log output. A read-only TextBox resolves this natively with `AppendText()`.
**Action:** For UI elements displaying continuous log output, always use a read-only `TextBox` with `AppendText()` instead of a `TextBlock` for better performance and text selection accessibility.
