
## 2024-04-09 - Optimize WPF Logging Performance
**Learning:** Using `TextBlock.Text += string` for frequent logging in WPF causes O(N^2) memory allocations and significant UI thread blocking because strings are immutable and the entire text is re-allocated and re-rendered on every update.
**Action:** Always use `TextBox.AppendText()` for UI logging scenarios. It provides O(1) appends, prevents UI freezes during heavy logs, and gives users the ability to select/copy text. To make it blend seamlessly, set `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`.
