## 2024-05-10 - O(N^2) String Allocations in WPF UI Logging
**Learning:** Using `TextBlock.Text += ...` inside a dispatcher for frequent UI logging creates an O(N^2) string allocation bottleneck that severely impacts performance and responsiveness during long-running background tasks. Throttling UI updates from background threads (e.g., using a Stopwatch) significantly reduces thread context switches.
**Action:** Always use `TextBox.AppendText()` or equivalent buffered UI controls for frequent appending, and throttle background progress reports to ~100ms.
