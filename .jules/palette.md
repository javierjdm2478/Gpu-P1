## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - Improve Log Output UX and Accessibility
**Learning:** For WPF UI logging and frequent text updates, using a `TextBlock` within a `ScrollViewer` with string concatenation causes memory and performance issues, and users cannot select or copy the log text.
**Action:** Use a read-only `TextBox` instead of `TextBlock` for log views. Call `TextBox.AppendText()` instead of string concatenation, configure it to look like a TextBlock (Background="Transparent", BorderThickness="0"), let it handle its own scrolling natively via `TextBox.ScrollToEnd()`, and include `AutomationProperties.Name` and `ToolTip` in the local language for accessibility.
