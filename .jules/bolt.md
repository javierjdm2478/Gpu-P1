## 2024-06-13 - O(N^2) UI Text Allocation
**Learning:** Using `TextBlock.Text +=` for frequent UI log updates creates O(N^2) memory allocation bottlenecks due to string immutability in .NET.
**Action:** Use `TextBox.AppendText()` with `IsReadOnly="True"` for high-frequency log updates to avoid unnecessary memory pressure and allow text selection.
