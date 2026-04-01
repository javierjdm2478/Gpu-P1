## 2024-05-18 - Optimize WPF UI logging performance
**Learning:** String concatenation on `TextBlock.Text` (`+=`) in WPF causes O(N²) memory allocations and severe UI thread bottlenecks as the log size grows.
**Action:** Replace `TextBlock` with `TextBox` for UI logs and use `TextBox.AppendText()` which is optimized for appending in O(1) time without massive string reallocation.
