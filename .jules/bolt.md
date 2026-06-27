## 2025-02-23 - WPF TextBlock Memory Leak
**Learning:** Appending strings with `+=` to a `TextBlock.Text` in WPF allocates a new string object each time, leading to O(N^2) memory consumption.
**Action:** Use a `TextBox` with `AppendText()` instead for high-frequency logging UI, along with styling it as read-only and borderless to simulate a text block without the performance hit.
