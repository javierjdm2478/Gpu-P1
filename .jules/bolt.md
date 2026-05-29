## 2024-05-24 - WPF UI Logging Performance
**Learning:** String concatenation (`TextBlock.Text +=`) for UI logging causes O(N²) memory allocations and full text re-renders in WPF.
**Action:** Use `TextBox.AppendText()` with a styled, read-only `TextBox` instead for efficient O(1) appends.
