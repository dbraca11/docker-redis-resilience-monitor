## 🧠 Lógica de Resiliencia (Self-Healing)
La aplicación implementa un patrón de **Retry Logic** que gestiona las dependencias de infraestructura:
1. Al iniciar, el servicio `monitor` intenta conectar con Redis.
2. Si Redis no está disponible (ej. arranque lento), la aplicación captura la excepción `ConnectionError`.
3. El sistema espera 3 segundos y reintenta indefinidamente hasta establecer la conexión.
4. Una vez conectado, inicia el reporte de estado operacional.

---
Proyecto desarrollado por **Darwin Braca**
