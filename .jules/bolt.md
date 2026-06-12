## 2024-05-24 - Efficient WPF Log Updating
**Learning:** In WPF, appending text to a `TextBlock` using string concatenation (`+=`) creates an O(N^2) memory allocation problem, because strings are immutable and a new string must be allocated and copied for each log entry.
**Action:** Use a `TextBox` with `IsReadOnly="True"` instead, and call its `AppendText()` method, which uses an internal `StringBuilder`-like mechanism and is significantly faster and more memory efficient for growing logs. Use `TextBox.Clear()` instead of assigning `""`.
