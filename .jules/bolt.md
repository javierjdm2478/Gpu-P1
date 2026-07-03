## 2024-05-24 - Optimize WPF UI logging performance
**Learning:** Using `TextBlock.Text +=` for frequent logging in WPF causes O(N^2) memory allocations and potential UI freezing because strings are immutable.
**Action:** Replace `TextBlock` and `ScrollViewer` with a `TextBox` (styled to look like a TextBlock) and use `TextBox.AppendText()` and `TextBox.Clear()` for highly efficient memory usage.
