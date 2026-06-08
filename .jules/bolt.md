## 2024-05-23 - WPF UI Logging Memory Optimization
**Learning:** Appending text to a `TextBlock` via string concatenation (`TextBlock.Text += ...`) causes O(N^2) memory allocations, creating a significant performance bottleneck for frequent log updates.
**Action:** Use `TextBox.AppendText()` with `IsReadOnly="True"` instead to prevent O(N^2) allocations and allow native `TextBox.ScrollToEnd()` scrolling.
