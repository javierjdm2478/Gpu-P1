## 2024-03-22 - O(N^2) WPF TextBlock UI Logging
**Learning:** Concatenating strings to a `TextBlock.Text` property inside a `Dispatcher.Invoke` loop creates a severe O(N^2) memory bottleneck that eventually blocks the UI thread. The system has to re-allocate and re-render the entire string on every log append.
**Action:** Always use a `TextBox` (with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic `TextBlock`) and use `AppendText()` to delegate rendering efficiency to the underlying text engine with O(1) amortized appends.
