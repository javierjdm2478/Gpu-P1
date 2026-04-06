
## 2024-04-06 - Replacing TextBlock with TextBox for logging UI components
**Learning:** Updating a `TextBlock` via string concatenation (`TextBlock.Text += ...`) frequently for log messages results in O(N^2) memory allocations and unnecessary layout recalculations, causing a UI thread bottleneck.
**Action:** Always prefer `TextBox.AppendText()` for updating frequent log outputs. Make it visually indistinguishable from a `TextBlock` using `Background="Transparent"`, `BorderThickness="0"`, and `IsReadOnly="True"`, and set appropriate `AutomationProperties.Name` and `ToolTip` for accessibility.
