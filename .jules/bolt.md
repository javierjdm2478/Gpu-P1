## 2026-03-08 - Use TextBox.AppendText for WPF UI logging
**Learning:** Concatenating strings to a `TextBlock.Text` (`+=`) in WPF causes O(N^2) memory allocations and freezes the UI thread when logging rapidly (e.g., copying files).
**Action:** Use `TextBox.AppendText()` configured as read-only for fast, append-only UI logging to eliminate allocation overhead and UI bottlenecks.
