## 2024-04-05 - Throttle UI updates in recursive file copy
**Learning:** Updating the UI on a per-file or naive count basis (e.g., `count % 10 == 0`) during fast recursive operations causes excessive UI thread context switches, leading to significant simulated execution time and UI blocking.
**Action:** Always throttle `IProgress<T>.Report` calls using a `Stopwatch` passed through recursive operations (with a ~100ms threshold) to batch progress updates and optimize performance.
