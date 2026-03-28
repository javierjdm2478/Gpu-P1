## 2026-03-28 - O(N^2) Memory Allocations in WPF TextBlock
**Learning:** Concatenating strings to `TextBlock.Text` (+=) for frequent UI updates (like logs) causes O(N^2) memory allocations and severely bottlenecks the UI thread in WPF applications.
**Action:** Always use `TextBox.AppendText()` for frequently updated logs. To maintain the visual appearance of a TextBlock, set `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` on the TextBox.
