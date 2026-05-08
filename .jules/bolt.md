## 2024-05-24 - WPF Log Performance
**Learning:** Using `TextBlock.Text +=` for frequent UI log updates in WPF causes O(N^2) memory allocations and significant performance degradation.
**Action:** Use `TextBox.AppendText()` with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic a TextBlock while maintaining O(1) append performance and allowing user text selection.
