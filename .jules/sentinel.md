## 2024-05-24 - [Fix Command Injection in PowerShell Execution]
**Vulnerability:** Command injection vulnerability via C# string interpolation (`$""`) passing untrusted variables (like `vmName`, extracted from WMI variables via user inputs/system state) directly into PowerShell commands executed via `ProcessStartInfo.Arguments`.
**Learning:** String interpolation or simple sanitization like replacing `'` with `''` is not adequate and can lead to command injection in PowerShell scripts depending on context and escaping edge cases.
**Prevention:** Always use `ProcessStartInfo.EnvironmentVariables` to pass untrusted arguments and reference them inside PowerShell scripts as `$env:VARNAME`.
