## 🧠 Lógica de Resiliencia (Self-Healing)
La aplicación implementa un patrón de **Retry Logic** que gestiona las dependencias de infraestructura:

Paso 1: Lo primero es bajar el código a su máquina local (o a una instancia de nube/Killercoda): git clone https://github.com/dbraca11/docker-redis-resilience-monitor.git
cd docker-redis-resilience-monitor

Paso 2: Gracias a que configuraste un archivo de orquestación, no necesitan instalar Python ni Redis en su computadora. Solo necesitan tener Docker instalado y ejecutar: docker-compose up --build

Paso 3: ¿Qué sucede durante la emulación? (Lo que verán en pantalla)
Orquestación: Docker levantará dos contenedores: uno con Redis y otro con tu script de Python (monitor_service).

Resiliencia en vivo: Si por alguna razón Redis tarda en arrancar, verán en la terminal los mensajes de tu script:
❌ [ESPERA] Redis no está listo. Reintentando en 3 segundos...

Self-healing: En cuanto Redis esté disponible, el script se conectará automáticamente y verán:
✅ [ÉXITO] Conectado a Redis
🚀 [REPORTE #1] Estado enviado: OPERACIONAL

Paso 4: Cómo verificar que los datos llegaron a Redis
Para demostrar que la emulación fue exitosa, pueden abrir otra terminal y entrar al contenedor de Redis para ver el valor que tu script guardó:

Bash
docker exec -it redis_db redis-cli get estado_sistema
Debería devolver: "OPERACIONAL".


---
Proyecto desarrollado por **Darwin Braca**

## 🗺️ Roadmap de Evolución del Proyecto

- [x] **Fase 1: Resiliencia & Monitoreo Base (Completado)**
  - [x] Contenerización de servicio Python y Redis con Docker Compose.
  - [x] Implementación de patrón de reintentos (*Retry Logic*) para tolerancia a fallas de arranque.
  - [x] Ingesta automática de métricas de estado en base de datos en memoria (Redis).

- [ ] **Fase 2: Observabilidad & Alertas**
  - [ ] Integración de Redis Exporter para métricas de rendimiento.
  - [ ] Implementación de Healthchecks nativos en `docker-compose.yml`.
  - [ ] Sistema de notificaciones automáticas ante fallas persistentes de conexión.

- [ ] **Fase 3: Escalamiento & Alta Disponibilidad**
  - [ ] Configuración de Redis Sentinel para conmutación por error (*Failover*).
  - [ ] Migración de arquitectura hacia despliegues gestionados en Kubernetes.

---

## 📊 Roadmap Gráfico

```mermaid
flowchart TD
    subgraph F1["Fase 1: Resiliencia Base (Completado)"]
        A1["Docker Compose Stack"]
        A2["Python Monitor + Retry Logic"]
        A3["Persistencia en Redis DB"]
    end

    subgraph F2["Fase 2: Observabilidad & Alertas"]
        B1["Docker Healthchecks"]
        B2["Redis Exporter Metrics"]
        B3["Alertas de Desconexión"]
    end

    subgraph F3["Fase 3: Alta Disponibilidad"]
        C1["Redis Sentinel Cluster"]
        C2["Estrategias Failover"]
        C3["Orquestación en Kubernetes"]
    end

    F1 --> F2 --> F3
