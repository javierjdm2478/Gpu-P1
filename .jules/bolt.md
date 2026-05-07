## 2024-05-07 - WPF TextBox AppendText for Performance
**Learning:** For WPF UI logging and frequent text updates, using string concatenation (`+=`) on a `TextBlock` causes O(N^2) memory allocations which severely degrades performance.
**Action:** Use `TextBox.AppendText()` instead. To mimic a `TextBlock`, set `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"`. Ensure `AutomationProperties.Name` and `ToolTip` are set for accessibility.
