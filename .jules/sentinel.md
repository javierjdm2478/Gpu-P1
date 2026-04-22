## 2025-03-17 - PowerShell Command and Script Injection
**Vulnerability:** The application was passing dynamic PowerShell commands to `powershell.exe` by constructing the `-Command` string using string interpolation. It was also embedding unsanitized user inputs (`vmName` and OS-retrieved `vhdxPath`) into these PowerShell scripts wrapped in single quotes (`'`). Both practices allowed for arbitrary PowerShell code injection if the strings contained `"` or `'`.
**Learning:** Using `Arguments = $"-Command \"{command}\""` for `ProcessStartInfo` is unsafe and susceptible to injection via double quotes. Embedding string variables inside PowerShell scripts surrounded by single quotes is also unsafe if the variables contain a single quote, which breaks out of the string context.
**Prevention:** Always use `ProcessStartInfo.ArgumentList` to securely pass command-line arguments to processes like `powershell.exe`. When dynamically embedding strings into a PowerShell script wrapped in single quotes, always escape the input by doubling single quotes (`input.Replace("'", "''")`).

## 2024-05-24 - Prevent PowerShell Command Injection
**Vulnerability:** Interpolating variables like `{vmName}` and WMI data like `{name}` directly into PowerShell strings executed via `powershell.exe -Command`. Even naive sanitization (e.g. replacing `'` with `''`) is bypassable.
**Learning:** `ProcessStartInfo.ArgumentList` passes commands directly to the shell. Any untrusted data needs to bypass command line parsing entirely to be safe.
**Prevention:** Pass untrusted variables through `ProcessStartInfo.EnvironmentVariables` and reference them natively inside the PowerShell script block using `$env:VARNAME`.
