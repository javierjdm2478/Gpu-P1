## 2024-05-14 - TextBox log append optimization
**Learning:** Using `TextBlock.Text +=` for frequent logging in WPF causes O(N^2) memory allocations and can freeze the UI thread on high volume. Replacing it with a styled `TextBox` and `AppendText()` significantly improves performance and gives the added bonus of selectable text.
**Action:** Always use `TextBox.AppendText()` or an `ObservableCollection` bound to an `ItemsControl` for appending text logs in WPF, never string concatenation on a `TextBlock`.
