## 2024-07-02 - Reemplazo de TextBlock con TextBox para Logs
**Learning:** En WPF, la concatenación continua de strings (`TextBlock.Text += ...`) causa asignaciones de memoria O(N^2) que degradan severamente el rendimiento en operaciones de registro frecuentes y prolongadas.
**Action:** Reemplazar `TextBlock` con `TextBox` y usar `AppendText()` para manejar logs, asegurando que `IsReadOnly="True"`, `Background="Transparent"`, y `BorderThickness="0"` estén configurados para mantener el aspecto visual y mejorar el rendimiento de memoria exponencialmente.
