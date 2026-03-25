## 2024-05-24 - WPF UI Logging Performance
**Learning:** Concatenating strings to a TextBlock.Text property in WPF causes O(N^2) memory allocations and freezes the UI thread during frequent updates.
**Action:** Always use TextBox.AppendText() with Background="Transparent", BorderThickness="0", and IsReadOnly="True" to mimic a TextBlock for high-frequency logging.
