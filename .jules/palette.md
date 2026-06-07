## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.

## 2024-06-07 - WPF Logging Accessibility and Selectability
**Learning:** Using `TextBlock` wrapped in a `ScrollViewer` for application logs prevents users from selecting or copying the text and limits screen reader accessibility. Additionally, string concatenation with `TextBlock.Text +=` causes O(N^2) memory allocations.
**Action:** Replace `TextBlock` logging with a read-only `TextBox` configured with `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"`. Use `TextBox.AppendText()` for efficient updates, and include `AutomationProperties.Name` and `ToolTip` to ensure full accessibility.
