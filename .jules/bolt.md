## 2025-06-29 - Optimize WPF Text Logging for Performance
**Learning:** WPF `TextBlock` is extremely inefficient for appending large amounts of text via string concatenation (`TextBlock.Text += ...`), causing O(N^2) memory allocations and potential UI freezes.
**Action:** Replace `TextBlock` with `TextBox` and use `TextBox.AppendText()` for O(1) appending in WPF logging scenarios to maintain UI responsiveness and reduce memory overhead, setting `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to retain the visual appearance of a TextBlock.
