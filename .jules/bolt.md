## 2024-07-01 - O(N²) Memory Allocation in WPF TextBlock Logging
**Learning:** Using string concatenation (+=) on a TextBlock.Text property for frequent logging in WPF causes O(N²) memory allocations, which degrades performance as the log grows.
**Action:** Use a TextBox with IsReadOnly="True" and AppendText() for UI logs, which handles large amounts of text updates more efficiently without reallocating the entire string.
