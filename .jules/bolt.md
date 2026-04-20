## 2026-03-09 - Prevent O(N²) String Concatenation in WPF Logging
**Learning:** In WPF, continually appending to a TextBlock using string concatenation (`TextBlock.Text += ...`) causes O(N²) memory allocations and severely degrades UI thread performance during frequent updates.
**Action:** Always use `TextBox.AppendText()` for logging or frequent text updates in WPF, and ensure the TextBox is styled to match the required look (e.g., `IsReadOnly=True`, `Background=Transparent`, `BorderThickness=0`).
