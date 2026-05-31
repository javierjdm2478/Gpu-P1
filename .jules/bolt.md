## 2024-05-31 - WPF TextBox Log Append Performance
**Learning:** For WPF UI logging and frequent text updates, using string concatenation (`+=`) on `TextBlock.Text` causes O(N^2) memory allocations and terrible performance for long logs.
**Action:** Use `TextBox.AppendText()` with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic a TextBlock while retaining O(1) append performance and native scrolling capabilities.
