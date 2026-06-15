## 2024-05-24 - WPF Log memory optimization
**Learning:** String concatenation and updating the Text property of TextBlock in WPF causes O(N^2) memory allocations and UI thread blocking during continuous updates.
**Action:** Use TextBox.AppendText() instead of TextBlock with string concatenation for frequently updated logs. Set IsReadOnly="True", Background="Transparent", BorderThickness="0", TextWrapping="Wrap", and VerticalScrollBarVisibility="Auto" to mimic a TextBlock while retaining optimal performance and allowing text selection.
