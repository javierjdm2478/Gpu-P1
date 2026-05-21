## 2024-05-21 - Optimize UI Text Logging
**Learning:** Using `Text += ...` or `AppendText` on a WPF TextBlock/TextBox for continuous high-frequency logging inside a loop is extremely inefficient, but O(N^2) memory allocations via `+=` string concatenation are especially bad for performance and memory usage compared to `TextBox.AppendText`.
**Action:** Always use `TextBox.AppendText()` or an `ObservableCollection` bound to an `ItemsControl` for continuous logging instead of string concatenation (`+=`) in WPF.
