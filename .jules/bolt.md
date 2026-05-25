## 2024-05-25 - Prevent O(N^2) memory allocations in WPF UI logging
**Learning:** String concatenation (`+=`) on a `TextBlock.Text` property causes O(N^2) memory allocations and forces the layout engine to re-measure and re-arrange the entire text, which can create a significant performance bottleneck during frequent log updates.
**Action:** Use `TextBox.AppendText()` with `IsReadOnly="True"` instead, which is optimized for appending text efficiently, and manage clearing with `TextBox.Clear()`.
