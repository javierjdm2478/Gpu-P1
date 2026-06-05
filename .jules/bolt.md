## 2025-02-12 - Optimize WPF Log Allocation
**Learning:** Using `TextBlock.Text += ...` in WPF creates O(N^2) memory allocations for high-frequency logs and slows down the UI thread.
**Action:** Always replace `TextBlock` + `ScrollViewer` with a `TextBox` using `TextBox.AppendText()` for appending high-frequency UI logs, and use `TextBox.Clear()` instead of assigning an empty string to minimize string allocation overhead.
