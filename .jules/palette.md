## 2024-05-17 - WPF Accessibility Improvements
**Learning:** TextBlock elements don't automatically associate with form inputs for screen readers. In WPF, using a Label with Target={Binding ElementName=ComponentName} establishes this relationship, while AutomationProperties.Name provides explicit descriptions for interactive elements like buttons and combo boxes.
**Action:** Always use Label with a Target binding instead of TextBlock for input descriptions in WPF, and ensure all buttons and interactive controls have AutomationProperties.Name and ToolTip defined.
