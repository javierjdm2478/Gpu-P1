
## 2024-05-24 - WPF UI Text Concatenation Performance
**Learning:** Using string concatenation (`+=`) on a `TextBlock` for frequent logging in WPF causes O(N²) memory allocations and degrades performance as the text grows.
**Action:** For UI logging, always use a `TextBox` with `TextBox.AppendText()`. To maintain a `TextBlock` visual style, set `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"`.
