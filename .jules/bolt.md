## 2024-05-24 - Avoid TextBlock.Text += for Logging
**Learning:** Using `TextBlock.Text += string` inside a frequent update loop (like `Dispatcher.Invoke`) causes O(N^2) string allocations and severe UI thread bottlenecks in WPF.
**Action:** Use a read-only `TextBox` with `Background="Transparent"` and `BorderThickness="0"` to visually mimic a `TextBlock`, and use its built-in `AppendText()` method for efficient O(1) appending.
