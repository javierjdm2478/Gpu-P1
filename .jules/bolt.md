## 2026-03-18 - Avoid O(N^2) memory allocations with TextBox.AppendText
**Learning:** Using TextBlock.Text += string causes O(N^2) memory allocations and UI thread performance bottlenecks. TextBox.AppendText() is faster for UI logging with frequent text updates.
**Action:** Use TextBox instead of TextBlock for frequent text appending in WPF.
