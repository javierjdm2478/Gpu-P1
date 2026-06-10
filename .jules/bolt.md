## 2024-06-10 - O(N^2) UI Text Allocation
**Learning:** Appending to a TextBlock (Text += "...") inside a loop or frequent update causes continuous reallocations and severe UI lag.
**Action:** Use a read-only TextBox and TextBox.AppendText() which leverages internal buffers and avoids string reallocation overhead for logs.
