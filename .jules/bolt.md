## 2024-05-24 - WPF Logging UI Thread Bottleneck
**Learning:** In WPF, concatenating strings to `TextBlock.Text` (`+=`) for frequent UI updates (like logs) causes O(N^2) memory allocations and severely blocks the UI thread as the string grows.
**Action:** Use `TextBox.AppendText()` instead of `TextBlock` for read-only logs with frequent updates to ensure O(1) appending and prevent UI freezing.
