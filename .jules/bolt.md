
## 2024-05-24 - Optimize UI logging for large outputs
**Learning:** Using string concatenation (`+=`) with a `TextBlock` for UI logging in WPF causes O(N^2) memory allocations and severe performance degradation as the log grows.
**Action:** Replace `TextBlock` and `ScrollViewer` with a `TextBox` configured to mimic a `TextBlock` (`IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, `VerticalScrollBarVisibility="Auto"`). Use `TextBox.AppendText()` for appending and `TextBox.Clear()` for clearing logs to achieve O(1) appending and prevent memory bloat.
