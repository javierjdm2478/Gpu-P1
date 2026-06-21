## 2024-06-21 - Optimize WPF UI Logging
**Learning:** String concatenation (+=) on WPF TextBlock.Text for frequent log updates causes O(N^2) memory allocations and can lock the UI thread.
**Action:** Use TextBox with IsReadOnly="True" and call TextBox.AppendText() to efficiently handle log streaming without massive reallocations.
