## 2025-03-17 - PowerShell Command and Script Injection
**Vulnerability:** The application was passing dynamic PowerShell commands to `powershell.exe` by constructing the `-Command` string using string interpolation. It was also embedding unsanitized user inputs (`vmName` and OS-retrieved `vhdxPath`) into these PowerShell scripts wrapped in single quotes (`'`). Both practices allowed for arbitrary PowerShell code injection if the strings contained `"` or `'`.
**Learning:** Using `Arguments = $"-Command \"{command}\""` for `ProcessStartInfo` is unsafe and susceptible to injection via double quotes. Embedding string variables inside PowerShell scripts surrounded by single quotes is also unsafe if the variables contain a single quote, which breaks out of the string context.
**Prevention:** Always use `ProcessStartInfo.ArgumentList` to securely pass command-line arguments to processes like `powershell.exe`. When dynamically embedding strings into a PowerShell script wrapped in single quotes, always escape the input by doubling single quotes (`input.Replace("'", "''")`).

## 2025-05-01 - Prevent Command Injection via ProcessStartInfo.EnvironmentVariables
**Vulnerability:** PowerShell command injection was possible despite escaping single quotes because the input variables could contain double quotes which broke out of the '-Command' context.
**Learning:** Using string interpolation for constructing ProcessStartInfo arguments, even with `.Replace("'", "''")`, is inherently unsafe and brittle.
**Prevention:** Always pass untrusted inputs through `ProcessStartInfo.EnvironmentVariables` and reference them as `$env:VARNAME` inside the PowerShell script block, completely avoiding string interpolation for command construction.
