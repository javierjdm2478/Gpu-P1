## 2024-04-18 - Optimize WPF TextBlock Concatenation
**Learning:** Concatenating strings to a WPF TextBlock using `+=` is an O(N²) operation that triggers heavy memory allocations and UI thread freezing, particularly noticeable during high-frequency updates like file copy progress reporting.
**Action:** Always use a `TextBox` with `AppendText()` for frequent UI text logging. Make it visually identical to a TextBlock by setting `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`.
