## 2024-05-24 - Optimize WPF Logging UI Updates
**Learning:** Concatenating strings to a WPF TextBlock.Text inside a loop causes O(N^2) memory allocations and UI thread performance bottlenecks.
**Action:** Use a read-only WPF TextBox and the `TextBox.AppendText()` method for efficient log appends instead of updating TextBlock.Text directly.