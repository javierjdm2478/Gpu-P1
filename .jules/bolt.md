## 2024-05-15 - WPF UI Thread Performance Issue with String Concatenation
**Learning:** Using `TextBlock.Text +=` for frequent logging in WPF causes an O(N^2) memory allocation problem and can block the UI thread as the text grows.
**Action:** Always use a `TextBox` or `RichTextBox` with `AppendText()` for appending log output in WPF applications to maintain linear time complexity and fluid UI performance.
