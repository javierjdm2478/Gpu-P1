## 2026-05-06 - File Copy Progress Throttling
**Learning:** Throttling `IProgress<string>.Report` calls using a Stopwatch during recursive file copies (e.g., with a 100ms threshold) significantly improves performance by reducing UI thread context switches, instead of blindly reporting every N files.
**Action:** When performing recursive/looping UI updates during I/O operations, use time-based throttling (Stopwatch) to prevent UI thread saturation.
