## 2023-10-24 - WPF TextBlock O(N^2) String Allocation Bottleneck
**Learning:** In WPF, using `TextBlock.Text +=` for logging creates an O(N²) performance bottleneck due to continuous string reallocation and full layout re-rendering. This is especially lethal when logging frequent progress updates (like driver file copying).
**Action:** Always use `TextBox.AppendText()` for appending log streams in WPF applications to utilize the native text engine's optimized append and scrolling capabilities.
