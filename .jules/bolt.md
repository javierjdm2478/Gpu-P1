## 2024-05-24 - Throttling IProgress<T>.Report in UI Applications
**Learning:** Calling IProgress<T>.Report too frequently inside a tight loop (like a file copy loop) causes massive overhead due to context switching and marshalling updates to the UI thread, which significantly slows down the background operation itself.
**Action:** Always throttle progress updates using a time-based approach (e.g., a Stopwatch checking for >100ms elapsed) or a less granular counter (but time is safer for varying task durations) to minimize cross-thread UI updates while keeping the application responsive.
