## 2024-06-16 - WPF TextBlock vs TextBox for Logging Performance
**Learning:** Using `TextBlock.Text +=` for frequent UI updates causes O(N^2) memory allocations because strings are immutable in C#. This can severely block the UI thread during high-frequency logging (like copying driver files).
**Action:** Always use `TextBox.AppendText()` for UI logs. To make it look like a TextBlock visually, set `IsReadOnly="True"`, `Background="Transparent"`, and `BorderThickness="0"`.
