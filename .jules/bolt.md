## 2025-01-24 - WPF Logging Performance
**Learning:** Updating a WPF `TextBlock` by string concatenation (`TextBlock.Text += string`) causes O(N^2) memory allocations on frequent text updates, significantly degrading performance over time.
**Action:** Use a `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` instead, and call `TextBox.AppendText()`. This drastically improves string manipulation performance and also enables the user to select/copy log output.
