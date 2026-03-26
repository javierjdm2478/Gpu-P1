
## 2024-05-18 - Avoid O(N^2) memory allocation in WPF TextBlock
**Learning:** In WPF, using `TextBlock.Text += "new string"` for frequently updated logs causes O(N^2) memory allocations and leads to UI thread performance bottlenecks as strings are immutable.
**Action:** Use a `TextBox` with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to visually mimic a `TextBlock`. Then, use `TextBox.AppendText()` instead, which efficiently appends text without recreating the entire string.
