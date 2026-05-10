## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2026-05-10 - WPF TextBox Performance & Accessibility
**Learning:** Using `TextBlock.Text +=` for frequent UI logging updates causes O(N^2) memory allocations and prevents users from selecting/copying text. It also needs accessibility attributes.
**Action:** Replace `TextBlock` with a `TextBox` using `AppendText()`. To maintain visual consistency, set `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"`. Ensure `AutomationProperties.Name` and `ToolTip` are included for accessibility.
