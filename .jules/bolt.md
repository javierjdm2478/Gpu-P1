## 2024-05-24 - Avoid redundant PowerShell process spawns
**Learning:** Invoking external processes like PowerShell from C# via `Process.Start` is slow. The path to the VM's VHDX file was being queried via PowerShell in step 4 to mount it, and then queried *again* via PowerShell in the `finally` block to dismount it.
**Action:** Cache the result of expensive external command invocations if the value will be needed again, particularly in cleanup or `finally` blocks, to reduce latency and save hundreds of milliseconds of execution time.
