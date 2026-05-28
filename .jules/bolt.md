## 2024-05-28 - WPF TextBlock Concatenation Performance
**Learning:** Frequent string concatenation (`+=`) in WPF `TextBlock.Text` causes O(N^2) memory allocations, degrading performance during rapid logging.
**Action:** Replace `TextBlock` with `TextBox` using `AppendText()` for efficient string updates, setting it to ReadOnly and removing surrounding ScrollViewer to leverage native scrolling.
