## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-06-10 - O(N^2) allocations for large log text blocks in WPF UI

**Learning:** String concatenation and TextBlock usage (`TextBlock.Text +=`) for continuous logging leads to massive memory allocations and freezes in WPF apps, plus prevents users from interacting with the text (copy/pasting errors). Using a `TextBox` with `IsReadOnly="True"` provides native scrolling and interaction while saving rendering costs.

**Action:** Whenever implementing a UI log viewer in WPF, opt for a read-only `TextBox` and use `AppendText` over string accumulation. Add `AutomationProperties.Name` and ensure it's keyboard accessible (already natively handled by TextBox).
