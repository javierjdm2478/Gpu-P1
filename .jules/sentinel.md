## 2024-05-15 - PowerShell Command Injection via String Interpolation
**Vulnerability:** The application was interpolating unescaped (or insufficiently escaped) user data (like `vmName` and `vhdxPath`) and hardware information (WMI queries) directly into PowerShell script strings executing via `powershell.exe -Command`.
**Learning:** Simple string replacement (`Replace("'", "''")`) is insufficient to prevent command injection because PowerShell's parsing rules inside `powershell.exe -Command` are complex and can be bypassed.
**Prevention:** Always use `ProcessStartInfo.EnvironmentVariables` to pass untrusted data to PowerShell scripts, and reference them as `$env:VARNAME` within the script.
