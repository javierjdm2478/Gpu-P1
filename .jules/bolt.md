## 2024-05-24 - Fix O(N^2) WPF Logging Bottleneck
**Learning:** Concatenating strings to a `TextBlock.Text` inside a logging method causes O(N^2) string allocations and severe UI thread blocking when many updates occur rapidly.
**Action:** Use a `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to visually mock a TextBlock, but allowing the use of `TextBox.AppendText()`, which manages internal text buffers efficiently without full reallocations.
