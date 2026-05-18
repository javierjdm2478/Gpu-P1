## 2025-02-18 - Improve LogMessage performance
**Learning:** For WPF UI logging with frequent text updates, using `TextBox.AppendText()` instead of string concatenation (`+=`) on a `TextBlock` prevents O(N^2) memory allocations.
**Action:** Use `TextBox` with `AppendText()` for UI logging instead of string concatenation.
