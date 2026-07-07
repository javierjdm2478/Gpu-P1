## 2024-03-30 - WPF Accessibility Enhancements
**Learning:** TextBlock elements used as labels in WPF are not accessible to screen readers, and interactive elements need AutomationProperties.Name and ToolTips.
**Action:** Replace TextBlocks functioning as labels with `<Label Target="{Binding ElementName=...}" Padding="0"/>` to maintain visual layout while adding screen reader support, and consistently add `AutomationProperties.Name` and `ToolTip` to inputs, buttons, and progress bars.
## 2024-05-24 - Selectable Log Text in WPF
**Learning:** Using a `TextBlock` for application logs in WPF prevents users from selecting and copying text (like error messages), hindering troubleshooting. Furthermore, appending text via string concatenation is inefficient compared to a `TextBox`.
**Action:** Replace log `TextBlock`s inside `ScrollViewer`s with a `TextBox` setting `IsReadOnly="True"`, `Background="Transparent"`, `BorderThickness="0"`, `TextWrapping="Wrap"`, and `VerticalScrollBarVisibility="Auto"`. Use `AppendText()` instead of `+=` for better performance and to natively allow users to copy text. Include `AutomationProperties.Name` and `ToolTip` in Spanish for accessibility.
