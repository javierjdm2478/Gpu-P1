## 2024-04-24 - Optimizing WPF Logging Performance
**Learning:** Using `TextBlock.Text += ...` in WPF creates O(N^2) memory allocations which can significantly hurt performance for frequent logging.
**Action:** Use `TextBox.AppendText()` instead, styling it with `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"` to mimic a TextBlock visually while keeping high performance appending and allowing text selection. Always include `AutomationProperties.Name` and `ToolTip` for accessibility.
