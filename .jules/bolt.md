## 2024-05-18 - Avoid O(N^2) Memory Allocations in WPF Logging
**Learning:** Concatenating strings to `TextBlock.Text` (using `+=`) for frequent UI updates (like logging) causes O(N^2) memory allocations and freezes the UI thread as the log grows.
**Action:** Use `TextBox.AppendText()` instead. To seamlessly mimic a TextBlock visually while providing text selection, set `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`.
