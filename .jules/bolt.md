## 2024-06-18 - Avoid TextBlock string concatenation O(N^2) allocations for logs
**Learning:** In WPF, using `TextBlock.Text +=` for logging creates many string allocations, leading to an O(N^2) performance hit as logs grow.
**Action:** Use a `TextBox` with `IsReadOnly="True"` and `TextBox.AppendText()` instead, which internally uses more efficient text storage and natively handles scrolling.
