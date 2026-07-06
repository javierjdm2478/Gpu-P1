## 2024-05-18 - Optimize UI Logger using TextBox
**Learning:** In WPF, string concatenation in a TextBlock inside a ScrollViewer (`TextBlock.Text += "..."`) for frequent log updates is an O(N^2) memory operation and blocks the UI thread.
**Action:** Replace `TextBlock` with a read-only `TextBox` and use `AppendText()`. This relies on the native WPF rendering and memory management of `TextBox` which avoids full string reallocation. Use `Clear()` instead of `Text = ""` and avoid redundant `ScrollViewer` containers since `TextBox` handles scrolling inherently.
