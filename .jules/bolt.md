## 2024-05-23 - O(N^2) UI Thread Memory Allocations in WPF Logs
**Learning:** Concatenating strings to a `TextBlock.Text` (using `+=`) for frequent log updates causes O(N^2) memory allocations and creates a significant performance bottleneck on the UI thread as the text grows.
**Action:** Replace `TextBlock` with `TextBox` (configured with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to mimic a TextBlock) and use `TextBox.AppendText()` to efficiently append logs.
