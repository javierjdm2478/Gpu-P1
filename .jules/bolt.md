## 2024-03-06 - Replacing TextBlock String Concatenation with TextBox.AppendText for Logs
**Learning:** Concatenating strings to a `TextBlock.Text` property via `+=` for frequent UI updates (like logs) creates severe O(N^2) memory allocations and bottlenecks the WPF UI thread. This is a crucial codebase-specific UI anti-pattern.
**Action:** Always use a read-only `TextBox` and its `.AppendText()` method for scrolling log displays in WPF to prevent UI freezing and excessive memory usage.
