## 2024-06-01 - WPF O(N^2) Logging Performance
**Learning:** Using `TextBlock.Text +=` for frequent UI logging creates O(N^2) memory allocations due to string immutability, which causes severe UI stutters and high memory pressure over time.
**Action:** Always use `TextBox.AppendText()` with `IsReadOnly="True"` instead of `TextBlock` for append-only logs in WPF to achieve O(1) appending and native scrolling.
