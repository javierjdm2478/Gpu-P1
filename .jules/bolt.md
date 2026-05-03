## 2024-05-23 - Throttling IProgress<string>.Report with Stopwatch
**Learning:** Frequently calling `IProgress<string>.Report` in a tight loop (like a recursive file copy) causes excessive UI thread context switches and drastically reduces performance, even if gated by simple counters (e.g. `count % 10 == 0`).
**Action:** Pass a `Stopwatch` down through recursive calls and throttle `Report` calls based on elapsed time (e.g., > 100ms threshold) to maintain UI responsiveness without sacrificing IO performance.
