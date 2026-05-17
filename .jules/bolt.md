## 2024-05-17 - Cache expensive external process results
**Learning:** Found a major bottleneck where `RunPowerShellCommand` (spawning a new `powershell.exe` process, which takes 100-300ms) was called twice for the exact same VHDX path: once to mount it and again in the `finally` block to dismount it.
**Action:** Always method-scope variables that store results of slow external API/process calls if that data is needed in cleanup/finally blocks.
