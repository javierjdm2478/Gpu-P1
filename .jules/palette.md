## 2025-01-28 - WPF Screen Reader Accessibility
**Learning:** Standard `TextBlock` elements used as field labels in WPF are not correctly associated with input fields by screen readers, and interactive elements need specific automation properties.
**Action:** Use `Label` with `Target="{Binding ElementName=TargetElement}"` instead of `TextBlock`, and apply `AutomationProperties.Name` and `ToolTip` to interactive elements like `ComboBox` and `Button` to improve screen reader support.
