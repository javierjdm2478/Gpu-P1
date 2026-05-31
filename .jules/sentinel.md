## 2025-03-17 - PowerShell Command and Script Injection
**Vulnerability:** The application was passing dynamic PowerShell commands to `powershell.exe` by constructing the `-Command` string using string interpolation. It was also embedding unsanitized user inputs (`vmName` and OS-retrieved `vhdxPath`) into these PowerShell scripts wrapped in single quotes (`'`). Both practices allowed for arbitrary PowerShell code injection if the strings contained `"` or `'`.
**Learning:** Using `Arguments = $"-Command \"{command}\""` for `ProcessStartInfo` is unsafe and susceptible to injection via double quotes. Embedding string variables inside PowerShell scripts surrounded by single quotes is also unsafe if the variables contain a single quote, which breaks out of the string context.
**Prevention:** Always use `ProcessStartInfo.ArgumentList` to securely pass command-line arguments to processes like `powershell.exe`. When dynamically embedding strings into a PowerShell script wrapped in single quotes, always escape the input by doubling single quotes (`input.Replace("'", "''")`).
## 2024-05-31 - Fix PowerShell Script Injection
**Vulnerability:** String interpolation in PowerShell command execution allowed script injection.
**Learning:** Passing parameters directly into command strings via `$"..."` or `$@""` is unsafe in C#. The proper way to pass untrusted inputs to PowerShell is by leveraging environment variables.
**Prevention:** Use `ProcessStartInfo.Environment` to pass parameters securely and reference them as `$env:VAR_NAME` within the PowerShell script.
