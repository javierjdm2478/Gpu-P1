## 2025-02-12 - WPF TextBlock Logging Performance
**Learning:** Using string concatenation (`+=`) on a WPF `TextBlock.Text` property for frequent logging causes O(N^2) memory allocations and forces the entire visual text to be re-measured and re-rendered on every update, severely degrading performance for long logs.
**Action:** Use `TextBox.AppendText()` with `IsReadOnly="True"` instead, which handles incremental text rendering efficiently and avoids recreating the entire string buffer. Always remove redundant `ScrollViewer` wrappers since `TextBox` natively handles scrolling.
