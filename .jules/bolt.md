## 2024-05-19 - Use TextBox instead of TextBlock for WPF logging
**Learning:** Appending text via `TextBox.AppendText()` instead of `TextBlock.Text += "..."` prevents an O(N^2) string allocation issue that negatively impacts memory and CPU performance during frequent logging.
**Action:** Always prefer `TextBox` over `TextBlock` for logs that update frequently. Use `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"`. `TextBox` manages its own scrolling natively so a wrapping `ScrollViewer` is unnecessary.
