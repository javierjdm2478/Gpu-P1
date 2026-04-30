## 2024-05-24 - Throttling UI Updates in Tight Loops
**Learning:** Frequent calls to `IProgress.Report()` inside tight loops (like recursive file copying of large directories) trigger excessive UI thread context switches, creating a severe performance bottleneck.
**Action:** Always throttle UI updates using `System.Diagnostics.Stopwatch.ElapsedMilliseconds > 100` instead of arbitrary file counts to maintain UI responsiveness without sacrificing execution speed.
