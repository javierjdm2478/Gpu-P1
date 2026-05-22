1.  **Format PR title & structure**: Format PR titles as '🛡️ Sentinel: [CRITICAL/HIGH] Fix [vulnerability type]', and structure descriptions with the exact sections '🚨 Severity', '💡 Vulnerability', '🎯 Impact', '🔧 Fix', and '✅ Verification'.

2.  **Verify the current change via git diff**:
    -   Use `run_in_bash_session` to run `git diff GpuPvSetup/MainWindow.xaml.cs`.
    -   Ensure that the replacement is correct and only the expected lines are modified.

3.  **Run dotnet build to ensure the code compiles**:
    -   Run `run_in_bash_session` with `dotnet build ./GpuPvSetup/GpuPvSetup.csproj -p:EnableWindowsTargeting=true -p:PublishSingleFile=false`.

4.  **Create / append to `.jules/sentinel.md` journal**:
    -   Create directory: `mkdir -p .jules`
    -   Append journal entry using the exact Sentinel format to record the PowerShell Command Injection vulnerability and the fix using `ProcessStartInfo.EnvironmentVariables` rather than string escaping.
        ```bash
        cat << 'EOF' >> .jules/sentinel.md
        ## 2024-05-24 - PowerShell Command Injection via String Interpolation
        **Vulnerability:** Untrusted user input (`vmName`) and OS-derived values were being interpolated directly into PowerShell command strings.
        **Learning:** Relying on simple string escaping (e.g., replacing `'` with `''`) is fragile and insufficient to prevent command injection in PowerShell scripts.
        **Prevention:** Always pass variables to PowerShell processes via `ProcessStartInfo.EnvironmentVariables` and reference them securely using `$env:VARNAME` inside the script.
        EOF
        ```

5.  **Run pre-commit instructions**:
    -   Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

6.  **Submit the code changes**:
    -   Commit and push using the `submit` tool with branch name `sentinel-fix-ps-injection`, a commit message, and a PR description containing the exact required sections (🚨 Severity, 💡 Vulnerability, 🎯 Impact, 🔧 Fix, ✅ Verification).
