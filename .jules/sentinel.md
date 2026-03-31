## 2024-05-18 - WMI Property Command Injection
**Vulnerability:** String interpolation of external properties (like WMI data) into PowerShell scripts passed to `powershell.exe -Command` creates command injection risks.
**Learning:** Even internal system data retrieved via WMI must be treated as untrusted and not interpolated directly into shell commands.
**Prevention:** Use environment variables (`startInfo.EnvironmentVariables`) to safely pass untrusted variables to PowerShell when `UseShellExecute = false`, and reference them inside the script as `$env:VARNAME`.
