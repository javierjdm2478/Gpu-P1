
## 2024-05-18 - WPF UI Logging Performance
**Learning:** Concatenating strings to `TextBlock.Text` (`+=`) for frequent UI updates causes O(N^2) memory allocations and freezes the UI thread.
**Action:** Use `TextBox.AppendText()` instead. To seamlessly mimic a `TextBlock` visually, apply `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`. Apply `AutomationProperties.Name` and `ToolTip` for accessibility.
