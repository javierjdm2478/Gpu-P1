## 2024-06-25 - Optimize UI logging memory allocation
**Learning:** Using `TextBlock.Text +=` for frequent log updates causes O(N^2) memory allocations and string copies.
**Action:** Use `TextBox.AppendText()` instead, styling it to mimic a `TextBlock` to maintain UI appearance while improving performance.
