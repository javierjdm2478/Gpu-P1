## 2024-05-30 - WPF Logging Performance Bottleneck
**Learning:** Using `TextBlock.Text +=` for frequent UI logging in WPF causes O(N^2) memory allocations and severe UI thread blocking as the text grows.
**Action:** Always use `TextBox.AppendText()` with `IsReadOnly="True"` for console-like logging components to ensure O(1) appending performance.