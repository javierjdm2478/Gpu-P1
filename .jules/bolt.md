## 2024-10-26 - Throttling IProgress UI Updates
**Learning:** Calling IProgress<string>.Report synchronously inside a tight loop (like recursive file copying) causes excessive UI thread context switches, severely degrading performance.
**Action:** Always throttle progress reporting in tight loops using a Stopwatch (e.g., every ~100ms) to batch updates and prevent UI thread starvation.
## 2024-10-26 - Consolidating PowerShell Commands
**Learning:** Spawning a new 'powershell.exe' process for every command execution incurs significant overhead and drastically slows down sequential operations.
**Action:** Consolidate multiple PowerShell commands into a single string (separated by semicolons) or script block to execute them in one process invocation.
