## 2024-05-15 - Throttling IProgress<string>.Report calls
**Learning:** In C# WPF applications, reporting progress via `IProgress<T>.Report` too frequently (e.g., inside tight loops like file copying) causes excessive UI thread context switches, leading to significant performance degradation and UI freezing.
**Action:** Use a `System.Diagnostics.Stopwatch` to throttle `IProgress<T>.Report` calls (e.g., to every 100ms) rather than relying on arbitrary item counts.
