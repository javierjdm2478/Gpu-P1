## 2024-05-24 - WPF Screen Reader Accessibility
**Learning:** In WPF applications, using `TextBlock` for input descriptions breaks screen reader accessibility because they lack semantic association with the input field.
**Action:** Use `Label` with a `Target` binding and `Padding="0"` to associate text with inputs without visual shifts, and add `AutomationProperties.Name` and `ToolTip` to all interactive controls.
