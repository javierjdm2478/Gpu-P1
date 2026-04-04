import re
with open("GpuPvSetup/MainWindow.xaml.cs", "r") as f:
    content = f.read()

old_method = """        private string RunPowerShellCommand(string command)
        {
            var startInfo = new ProcessStartInfo
            {
                FileName = "powershell.exe",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };"""

new_method = """        private string RunPowerShellCommand(string command, Dictionary<string, string>? envVars = null)
        {
            var startInfo = new ProcessStartInfo
            {
                FileName = "powershell.exe",
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            if (envVars != null)
            {
                foreach (var kvp in envVars)
                {
                    startInfo.EnvironmentVariables[kvp.Key] = kvp.Value;
                }
            }"""

content = content.replace(old_method, new_method)
with open("GpuPvSetup/MainWindow.xaml.cs", "w") as f:
    f.write(content)
