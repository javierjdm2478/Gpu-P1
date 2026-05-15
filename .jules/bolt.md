## 2024-05-15 - Optimize WPF Logging Memory Usage
**Learning:** Appending to a `TextBlock.Text` in WPF creates O(N²) memory allocations because strings are immutable in C# and WPF has to re-parse the entire string for rendering on every update. In operations that log frequently (like file copying), this causes massive UI thread blocking and memory churn.
**Action:** Replace `TextBlock` with a read-only `TextBox` and use `AppendText()` for appending logs, which handles text efficiently and allows the UI to stay responsive during high-frequency log events.
