
## 2026-04-14 - Optimize WPF Logging UI Updates
**Learning:** Concatenating strings to a `TextBlock.Text` inside a loop or frequently called method causes O(N^2) memory allocations and performance degradation because strings in C# are immutable.
**Action:** Always use `TextBox.AppendText()` for frequently updated UI logs, configuring it to mimic a TextBlock visually (`Background="Transparent"`, `BorderThickness="0"`, `IsReadOnly="True"`) to avoid unnecessary memory overhead.
