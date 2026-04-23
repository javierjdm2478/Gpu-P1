## 2026-04-23 - Use TextBox.AppendText for O(1) logging performance
**Learning:** Using `TextBlock.Text += "..."` for frequent log updates causes O(N²) memory allocations and high UI thread overhead due to string immutability.
**Action:** Use a `TextBox` with `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, and `TextWrapping="Wrap"` to mimic a `TextBlock`, and use `TextBox.AppendText()` to achieve O(1) append performance. Always add `AutomationProperties.Name` and `ToolTip` for accessibility.
