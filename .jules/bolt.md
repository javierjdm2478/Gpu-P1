## 2024-05-24 - String Concatenation O(N^2) in UI Logs
**Learning:** Using `TextBlock.Text +=` for frequent UI logging creates an O(N^2) memory allocation bottleneck, which can severely impact performance during long-running tasks like recursive file copies or PowerShell executions that generate continuous output.
**Action:** Replace `TextBlock` with `TextBox` configured as read-only (`IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`) and use `TextBox.AppendText()` instead, which is optimized for appending strings without reallocating the entire buffer.
