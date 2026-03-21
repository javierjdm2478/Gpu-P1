## 2026-03-21 - Accessible WPF Controls
**Learning:** TextBlock elements don't provide screen reader context for adjacent inputs. Interactive elements without AutomationProperties.Name are not properly announced.
**Action:** Use Label with Target="{Binding ElementName=InputName}" (and Padding="0" to prevent shifts) instead of TextBlock for input descriptions. Add AutomationProperties.Name and ToolTip to all interactive elements.
