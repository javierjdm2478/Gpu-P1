## 2024-06-28 - Rendimiento en registros de WPF
**Learning:** El uso de concatenación de strings (`+=`) en `TextBlock` para registros frecuentes causa reasignaciones O(N^2) en memoria, afectando el rendimiento del hilo principal (UI).
**Action:** Utilizar `TextBox` con `AppendText()` y `Clear()` junto a propiedades de solo lectura para simular visualmente un `TextBlock`, logrando actualizaciones eficientes y nativas en WPF.
