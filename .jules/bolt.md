## 2024-04-16 - Prevent O(N²) memory allocations in UI logs
**Learning:** Concatenating strings to `TextBlock.Text` (+=) for frequent UI logs causes O(N²) memory allocations and freezes the UI thread during long operations.
**Action:** Use `TextBox.AppendText()` instead of `TextBlock.Text +=`. To visually mimic a TextBlock, set `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"` on the TextBox.
