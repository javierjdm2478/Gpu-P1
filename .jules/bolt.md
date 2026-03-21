## 2024-05-20 - Prevent O(N^2) Allocations in WPF UI Logging
**Learning:** For WPF UI logging and frequent text updates, use `TextBox.AppendText()` rather than concatenating strings to `TextBlock.Text` (+=) to prevent O(N^2) memory allocations and UI thread performance bottlenecks.
**Action:** Always prefer `TextBox.AppendText()` over `TextBlock.Text +=` for appending text frequently.
