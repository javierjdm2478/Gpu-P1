## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-04-25 - WPF Log Text Selectability
**Learning:** Using a TextBlock for log output prevents users from selecting and copying text, which is frustrating for troubleshooting. Furthermore, missing AutomationProperties makes it inaccessible to screen readers.
**Action:** Replace LogTextBlock with a read-only TextBox (with transparent background and no border) and use `.AppendText()` to allow text selection. Always add `AutomationProperties.Name` and `ToolTip` for accessibility.
