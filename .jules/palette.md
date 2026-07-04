## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - [Replace ScrollViewer/TextBlock with TextBox for Logs]
**Learning:** For WPF UI logging, using a TextBlock with string concatenation (+-) causes O(N^2) memory allocations and prevents users from selecting or copying text.
**Action:** Replaced TextBlock wrapped in ScrollViewer with a native TextBox with IsReadOnly="True" and TextWrapping="Wrap", utilizing TextBox.AppendText() for efficient appending and native scrolling capability, keeping Spanish accessibility descriptions.
