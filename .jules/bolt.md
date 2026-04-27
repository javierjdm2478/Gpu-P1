## 2024-04-27 - O(N^2) TextBlock string allocations in WPF
**Learning:** Using `TextBlock.Text +=` for appending logs causes O(N^2) memory allocations and lag as the string length increases. WPF TextBlock does not support incremental appends.
**Action:** For UI logging, always use `TextBox.AppendText()` instead, styling it to look like a TextBlock (`IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`).
