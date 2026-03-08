## 2025-03-08 - Prevent Command Injection in PowerShell Execution
**Vulnerability:** Execution of raw, unsanitized strings in PowerShell commands (command injection) via `ProcessStartInfo.Arguments` with dynamic inputs like `VMName` and `VhdxPath` being unsafely concatenated.
**Learning:** Concatenating user inputs into a single `Arguments` string allows for escaping contexts and injecting arbitrary commands if the user supplies crafted values (e.g. `'; Invoke-Expression 'malicious'; '`).
**Prevention:** Always use `ProcessStartInfo.ArgumentList` to pass the command and arguments separately to PowerShell, and escape single quotes for dynamic inputs by replacing them with two single quotes (`'` -> `''`) when used inside script blocks.
