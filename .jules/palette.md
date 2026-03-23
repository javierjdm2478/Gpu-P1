## 2024-05-24 - Accessible Input Labels in WPF
**Learning:** Using a simple `TextBlock` for a label doesn't link it for screen readers. In WPF, to correctly associate a label with its input without altering the visual layout, use a `<Label>` element with `Target="{Binding ElementName=TargetControlName}"` and apply `Padding="0"` to avoid visual shifts compared to `TextBlock`.
**Action:** Always prefer `<Label Target="...">` with `Padding="0"` over `TextBlock` for form fields in WPF, and accompany interactive elements with `AutomationProperties.Name` and `ToolTip`.
