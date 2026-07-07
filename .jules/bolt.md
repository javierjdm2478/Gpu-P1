## 2024-05-24 - Optimize WPF Logging Performance
**Learning:** In WPF, appending to a `TextBlock.Text` inside a loop or frequently called method creates a new string every time, leading to O(N^2) time complexity and massive memory allocations. `TextBox` handles large volumes of text much more efficiently than `TextBlock` for log views.
**Action:** Replace `TextBlock` with a read-only `TextBox` and use `TextBox.AppendText()` instead of `Text +=` for frequent logging updates to improve UI responsiveness and memory usage.
