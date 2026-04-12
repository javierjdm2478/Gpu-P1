## 2024-04-12 - WPF TextBlock String Concatenation Bottleneck
**Learning:** Using `TextBlock.Text += ...` for frequent UI logging creates an O(N^2) memory allocation bottleneck due to immutable string creation on every append.
**Action:** Always use `TextBox` with `AppendText()` for logs, and style it with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to mimic a `TextBlock` seamlessly while maintaining high performance.
