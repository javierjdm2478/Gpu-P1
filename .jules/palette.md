## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-05-05 - Selectable Log Text for Better UX
**Learning:** Using TextBlock for application log outputs prevents users from selecting and copying text, which degrades UX and hinders troubleshooting or sharing logs. TextBlock log concatenation is also poor for performance and accessibility.
**Action:** Replace TextBlock with a read-only TextBox (with transparent background and no borders) for text logs. This enables text selection, avoids O(N^2) memory issues via AppendText(), and improves accessibility when AutomationProperties.Name and ToolTips are included.
