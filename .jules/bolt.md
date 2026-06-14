## 2024-06-14 - Optimize WPF Logging Performance
**Learning:** Appending to a `TextBlock.Text` inside a `ScrollViewer` using string concatenation (`+=`) in WPF causes O(N^2) memory allocations and terrible UI thread performance for frequent log updates.
**Action:** Always use `TextBox.AppendText()` with `IsReadOnly="True"` for log viewers instead of `TextBlock.Text += ...`. `TextBox` handles scrolling natively (`ScrollToEnd()`) and avoids copying the entire string on every append.
