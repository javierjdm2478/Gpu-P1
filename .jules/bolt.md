## 2024-06-26 - Optimize WPF Logging to Prevent O(N^2) Allocations
**Learning:** Using string concatenation (`+=`) and `TextBlock` for append-only UI logging creates O(N^2) memory allocations, slowing down performance and consuming unnecessary memory for frequent logging.
**Action:** Use `TextBox.AppendText()` with `IsReadOnly="True"` and `Background="Transparent"` to natively handle large text appends efficiently and enable user selection/copying without degrading performance.
