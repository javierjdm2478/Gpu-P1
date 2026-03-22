## 2024-05-24 - Improve screen reader accessibility for WPF elements
**Learning:** WPF TextBlocks for form labels fail to associate with inputs for screen readers. Buttons and input elements also lack default screen reader cues if not properly labeled.
**Action:** Always replace TextBlock with Label + Target binding (using Padding="0" to avoid visual shifts) for form inputs, and ensure all interactive elements have AutomationProperties.Name and ToolTip attributes.
