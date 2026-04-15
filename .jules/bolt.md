## 2026-04-15 - Replace UI logging TextBlock with TextBox for O(1) appending
**Learning:** Concatenating strings to a WPF TextBlock.Text property inside a high-frequency logging loop causes O(N^2) memory allocations and unnecessary layout recalculations.
**Action:** Use TextBox.AppendText() with `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` to achieve the same visual look with O(1) performance overhead while enabling text selection.
