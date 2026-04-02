## 2026-03-24 - Optimize WPF Logging
**Learning:** For WPF UI logging and frequent text updates, use 'TextBox.AppendText()' rather than concatenating strings to 'TextBlock.Text' (+=) to prevent O(N^2) memory allocations and UI thread performance bottlenecks. To visually mimic a TextBlock seamlessly, set `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` on the TextBox.
**Action:** Always prefer `TextBox.AppendText()` or `TextBox.AppendText()` with read-only properties over `TextBlock` for append-only logs in WPF.
