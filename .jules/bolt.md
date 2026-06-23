## 2024-06-23 - Prevent O(N^2) memory allocations for WPF UI logging
**Learning:** In WPF, using a `TextBlock` and appending to its `Text` property with `+=` causes O(N^2) string allocations and performance degradation during frequent updates.
**Action:** Use a `TextBox` with `IsReadOnly="True"` and use `TextBox.AppendText()` for O(N) amortized logging performance, and `TextBox.Clear()` instead of assigning an empty string. `TextBox` natively handles scrolling via `ScrollToEnd()`.
