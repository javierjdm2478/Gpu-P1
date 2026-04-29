
## 2024-04-29 - [UI Progress Throttling in High-Frequency I/O]
**Learning:** Using arbitrary counts (like `count % 10`) for reporting progress during fast I/O operations (like copying many small driver files) causes excessive `IProgress<T>.Report` calls. This forces numerous context switches to the UI thread via `Dispatcher.Invoke`, significantly degrading overall execution speed and freezing the UI.
**Action:** Instead of counting iterations, pass a `Stopwatch` through recursive calls and throttle progress updates based on elapsed time (e.g., >100ms). This minimizes UI thread overhead while keeping the progress report smooth.
