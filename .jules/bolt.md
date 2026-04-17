## 2026-03-14 - WPF TextBlock vs TextBox O(N^2) memory allocation
**Learning:** Using `TextBlock.Text += ...` for frequent UI log updates in WPF causes O(N^2) string allocations, leading to memory bloat and UI thread bottlenecks.
**Action:** Always use `TextBox` with `IsReadOnly="True"` and `AppendText()` for frequently updated text logs in WPF.
