## 2023-10-24 - Optimizing WPF text logging performance
**Learning:** Using `TextBlock.Text += ...` for frequent UI log updates in WPF causes O(N^2) memory allocations and freezes the UI thread.
**Action:** Use a `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` instead, and use `TextBox.AppendText()` to achieve O(1) appending performance without losing the visual appearance of a TextBlock.
