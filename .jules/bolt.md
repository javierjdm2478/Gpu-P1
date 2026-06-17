## 2024-05-25 - Prevent O(N^2) memory allocations in WPF UI logging
**Learning:** Using TextBlock with string concatenation (+=) for frequent UI logging creates an O(N^2) performance bottleneck due to continuous string reallocation.
**Action:** Use TextBox.AppendText() instead of TextBlock string concatenation to drastically reduce memory allocations during UI updates.
