## 2025-02-23 - TextBox.AppendText() for O(1) String Appends in WPF
**Learning:** Using `+=` to append text to a `TextBlock.Text` property in a WPF UI logging control triggers O(N^2) memory allocations and string copies, which can cause significant GC pressure and UI thread hitching during heavy logging tasks like file copying.
**Action:** Replace `TextBlock` with a read-only `TextBox` mimicking a text block, and use `TextBox.AppendText()` for optimized internal string buffering instead of concatenated strings. Use `TextBox.Clear()` instead of assigning `""`.
