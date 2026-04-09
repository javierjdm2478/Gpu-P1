## 2025-03-17 - PowerShell Command and Script Injection
**Vulnerability:** The application was passing dynamic PowerShell commands to `powershell.exe` by constructing the `-Command` string using string interpolation. It was also embedding unsanitized user inputs (`vmName` and OS-retrieved `vhdxPath`) into these PowerShell scripts wrapped in single quotes (`'`). Both practices allowed for arbitrary PowerShell code injection if the strings contained `"` or `'`.
**Learning:** Using `Arguments = $"-Command \"{command}\""` for `ProcessStartInfo` is unsafe and susceptible to injection via double quotes. Embedding string variables inside PowerShell scripts surrounded by single quotes is also unsafe if the variables contain a single quote, which breaks out of the string context.
**Prevention:** Always use `ProcessStartInfo.ArgumentList` to securely pass command-line arguments to processes like `powershell.exe`. When dynamically embedding strings into a PowerShell script wrapped in single quotes, always escape the input by doubling single quotes (`input.Replace("'", "''")`).

## 2025-03-17 - Secure PowerShell Execution
**Vulnerability:** Passing untrusted data to PowerShell via `-Command` using string interpolation is vulnerable to command injection. Even when escaping single quotes, the argument can break out if other escape characters or edge cases apply.
**Learning:** You must not concatenate or interpolate dynamic variables into powershell command scripts.
**Prevention:** Use `ProcessStartInfo.EnvironmentVariables` to pass untrusted data to PowerShell, referencing the variables in the script via `$env:VAR_NAME`.
