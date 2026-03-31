## 2025-03-13 - [WPF Logging Performance]
**Learning:** Using `TextBlock.Text +=` for frequent UI log updates creates an O(N^2) string allocation bottleneck that freezes the UI thread.
**Action:** Always use `TextBox.AppendText()` with `IsReadOnly="True"` instead of `TextBlock` for append-heavy operations in WPF to avoid GC pressure and UI freezing.
