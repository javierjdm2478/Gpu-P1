## 2024-05-04 - Prevent O(N^2) allocations in WPF logging
**Learning:** Using `TextBlock.Text +=` for frequent UI text updates causes O(N^2) memory allocations and lag.
**Action:** Use `TextBox.AppendText()` with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic a TextBlock while providing efficient O(1) text appending and allowing users to select/copy text.
