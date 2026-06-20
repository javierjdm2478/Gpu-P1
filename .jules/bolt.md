## 2024-06-20 - WPF O(N^2) String Concatenation Bottleneck
**Learning:** Using `TextBlock.Text +=` for UI logging in WPF causes O(N^2) memory allocations and massive re-rendering overhead on each append.
**Action:** Always use `TextBox.AppendText()` for frequently updated text logs, styling it with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic a TextBlock while retaining O(1) append performance.
