## 2025-02-23 - TextBox AppendText Optimization for WPF Logs
**Learning:** In WPF, using string concatenation (`+=`) on a `TextBlock` for logs causes O(N^2) memory allocations and slow performance because it recreates the entire string every time. Using `TextBox.AppendText()` is an O(1) operation.
**Action:** Use `TextBox` with `AppendText()` instead of `TextBlock` with string concatenation for logging.
