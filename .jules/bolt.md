## 2024-04-02 - WPF TextBlock String Concatenation Performance
**Learning:** Concatenating strings to a WPF TextBlock's Text property (`TextBlock.Text += ...`) causes O(N^2) memory allocations and can freeze the UI thread during frequent updates like logging.
**Action:** Use `TextBox` with `AppendText()` instead of `TextBlock` for logs. To maintain the visual appearance, set `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`.
