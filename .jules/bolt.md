
## 2024-04-01 - O(N²) Memory Allocation in WPF Logging
**Learning:** Concatenating strings to a `TextBlock.Text` property using `+=` inside a frequent update loop (like logging) causes O(N²) memory allocations and forces the UI thread to re-render the entire string on every update, creating severe performance bottlenecks.
**Action:** Use a `TextBox` with `AppendText()` instead of `TextBlock` for logs. To maintain the visual appearance of a plain text block, set `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`.
