## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - Interactive Output Logs
**Learning:** For WPF UI logging and frequent text updates, use `TextBox` instead of `TextBlock` wrapped in a `ScrollViewer`. Using `TextBox.AppendText()` instead of string concatenation (`+=` on `TextBlock.Text`) prevents O(N^2) memory allocations and allows users to select/copy log text.
**Action:** Always prefer `TextBox` configured to mimic a `TextBlock` (`IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, `VerticalScrollBarVisibility="Auto"`) for logging output. Ensure `AutomationProperties.Name` and `ToolTip` are set for accessibility.
