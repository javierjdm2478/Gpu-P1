import codecs

with codecs.open('./GpuPvSetup/MainWindow.xaml.cs', 'r', 'utf-8-sig') as f:
    content = f.read()

search_str = """        private void CopyDirectory(string sourceDir, string destinationDir, IProgress<string> progress)
        {
            var dir = new DirectoryInfo(sourceDir);

            if (!dir.Exists)
                throw new DirectoryNotFoundException($"Source directory not found: {dir.FullName}");

            DirectoryInfo[] dirs = dir.GetDirectories();
            Directory.CreateDirectory(destinationDir);

            FileInfo[] files = dir.GetFiles();
            int totalFiles = files.Length;
            int count = 0;

            foreach (FileInfo file in files)
            {
                string targetFilePath = Path.Combine(destinationDir, file.Name);
                file.CopyTo(targetFilePath, true);
                count++;

                // Actualizar progreso sin saturar la UI (cada 10 archivos)
                if (count % 10 == 0 || count == totalFiles)
                {
                     progress.Report($"Copiando archivos del driver... ({count}/{totalFiles})");
                }
            }

            foreach (DirectoryInfo subDir in dirs)
            {
                string newDestinationDir = Path.Combine(destinationDir, subDir.Name);
                CopyDirectory(subDir.FullName, newDestinationDir, progress); // No mostramos sub-progreso para simplificar
            }
        }"""

replace_str = """        private void CopyDirectory(string sourceDir, string destinationDir, IProgress<string> progress, System.Diagnostics.Stopwatch? stopwatch = null)
        {
            if (stopwatch == null)
            {
                stopwatch = System.Diagnostics.Stopwatch.StartNew();
            }

            var dir = new DirectoryInfo(sourceDir);

            if (!dir.Exists)
                throw new DirectoryNotFoundException($"Source directory not found: {dir.FullName}");

            DirectoryInfo[] dirs = dir.GetDirectories();
            Directory.CreateDirectory(destinationDir);

            FileInfo[] files = dir.GetFiles();
            int totalFiles = files.Length;
            int count = 0;

            foreach (FileInfo file in files)
            {
                string targetFilePath = Path.Combine(destinationDir, file.Name);
                file.CopyTo(targetFilePath, true);
                count++;

                // Actualizar progreso sin saturar la UI (cada 100ms o al finalizar)
                if (stopwatch.ElapsedMilliseconds > 100 || count == totalFiles)
                {
                     progress.Report($"Copiando archivos del driver... ({count}/{totalFiles})");
                     stopwatch.Restart();
                }
            }

            foreach (DirectoryInfo subDir in dirs)
            {
                string newDestinationDir = Path.Combine(destinationDir, subDir.Name);
                CopyDirectory(subDir.FullName, newDestinationDir, progress, stopwatch); // No mostramos sub-progreso para simplificar
            }
        }"""

content = content.replace(search_str, replace_str)

with codecs.open('./GpuPvSetup/MainWindow.xaml.cs', 'w', 'utf-8-sig') as f:
    f.write(content)
