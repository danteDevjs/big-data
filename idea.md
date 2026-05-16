# Proyecto: Red Mesh Autónoma de Emergencia

# Idea principal

Crear una red mesh autónoma compuesta por nodos portátiles capaces de:

- descubrir otros nodos automáticamente,
- formar una red sin internet,
- retransmitir mensajes,
- compartir ubicación GPS,
- transmitir telemetría y signos vitales,
- enviar alertas de emergencia,
- reorganizarse dinámicamente.

---

# Objetivo

Desarrollar una infraestructura de comunicación resiliente para escenarios donde:

- internet falla,
- no hay señal celular,
- existen terremotos,
- incendios,
- desastres naturales,
- zonas rurales aisladas.

---

# Concepto central

Cada nodo funciona como:

- router,
- repetidor,
- microcomputador,
- sensor,
- radio de comunicación.

---

# Funcionamiento básico

1. El nodo se enciende.
2. Busca otros nodos cercanos.
3. Detecta vecinos automáticamente.
4. Intercambia información.
5. Forma una red mesh dinámica.
6. Comienza a retransmitir datos.

---

# Características principales

- autónomo,
- portátil,
- modular,
- resiliente,
- descentralizado,
- auto-organizable,
- auto-reparable.

---

# Mesh Network

## Qué es

Una red donde cada nodo puede:

- comunicarse con otros,
- retransmitir mensajes,
- expandir cobertura.

---

# Diferencia con red tradicional

## Red normal

Cliente → Router → Internet

## Red Mesh

A ↔ B ↔ C ↔ D

---

# Self-Organizing Network

La red:

- descubre nodos automáticamente,
- crea rutas dinámicamente,
- no requiere configuración manual.

---

# Self-Healing

Si un nodo cae:

A → B → C

B falla

A → D → C

La red recalcula rutas automáticamente.

---

# Hardware del nodo

## Componentes principales

- ESP32,
- módulo LoRa SX1276/SX1262,
- batería,
- antena,
- GPS,
- sensores opcionales.

---

# Sensores posibles

- ritmo cardíaco,
- temperatura,
- humo,
- gas,
- acelerómetro,
- GPS,
- movimiento.

---

# Tecnología principal

# LoRa

## Características

- largo alcance,
- bajo consumo,
- resistente,
- baja velocidad,
- ideal para emergencias.

---

# LoRa NO está pensado para

- video,
- streaming,
- llamadas HD.

---

# LoRa SÍ funciona bien para

- mensajes,
- alertas,
- GPS,
- telemetría,
- sensores.

---

# Tipos de mensajes

## 1. Mensajes críticos

- SOS,
- incendio,
- evacuación,
- herido,
- ambulancia.

Máxima prioridad.

---

## 2. Telemetría

- GPS,
- signos vitales,
- temperatura,
- estado nodo.

---

## 3. Mensajes normales

Chat básico de menor prioridad.

---

# Protocolo de emergencia

# Emergency Protocol Dictionary

Sistema de códigos compactos para emergencias.

## Ejemplo

| Código | Significado |
|---|---|
| 0x01 | estoy bien |
| 0x02 | necesito ayuda |
| 0x03 | incendio |
| 0x04 | evacuación |
| 0x05 | atrapado |

---

# Ventajas de mensajes compactos

- menos tráfico,
- más velocidad,
- menos congestión,
- menor consumo energético,
- mayor eficiencia.

---

# Routing

## Cómo viajan los mensajes

A → B → C → D

Cada nodo:
- recibe,
- analiza,
- retransmite.

---

# Multi-Hop Networking

Los mensajes saltan entre nodos para ampliar cobertura.

---

# Neighbor Discovery

Los nodos envían señales de presencia:

"Estoy aquí"

Con eso:
- detectan vecinos,
- construyen rutas,
- crean topología de red.

---

# Routing dinámico

La red elige rutas usando:

- señal,
- congestión,
- batería,
- estabilidad,
- cantidad de saltos.

---

# Priorización de tráfico

No todos los mensajes tienen la misma prioridad.

## Prioridades

| Prioridad | Ejemplo |
|---|---|
| máxima | SOS |
| alta | ubicación |
| media | telemetría |
| baja | chat |

---

# Clusters

La red puede dividirse en grupos para reducir congestión.

## Ejemplo

[Cluster Norte]
↓
[Super Nodo]
↓
[Cluster Centro]

---

# Ventajas de clusters

- menos congestión,
- mejor escalabilidad,
- tráfico organizado,
- mayor estabilidad.

---

# Celulares y PCs

Los celulares NO usan LoRa directamente.

Se conectan mediante:

- WiFi,
- Bluetooth.

---

# Arquitectura

Celular ↔ Nodo ↔ Mesh Network

---

# Resultado

Incluso sin internet:

- mensajes funcionan,
- GPS funciona,
- alertas funcionan,
- comunicación sigue activa.

---

# Store and Forward

Si un nodo no puede enviar inmediatamente:

1. guarda el mensaje,
2. espera conexión,
3. lo retransmite después.

---

# Aplicaciones reales

- terremotos,
- incendios,
- minería,
- rescate,
- zonas rurales,
- catástrofes naturales.

---

# Problema principal

La dificultad real NO es conectar nodos.

La dificultad real es:

- evitar congestión,
- evitar colisiones,
- mantener estabilidad,
- escalar correctamente.

---

# Soluciones planteadas

- clusters,
- prioridades,
- routing inteligente,
- mensajes compactos,
- super nodos,
- retransmisión selectiva.

---

# Conceptos técnicos involucrados

- mesh networking,
- routing dinámico,
- sistemas distribuidos,
- LoRa,
- IoT,
- edge computing,
- DTN,
- self-healing,
- protocolos de emergencia.

---

# Visión final

Crear un sistema autónomo de comunicación resiliente capaz de:

- mantener comunicación en desastres,
- conectar civiles y rescatistas,
- compartir ubicación,
- transmitir alertas críticas,
- funcionar sin internet,
- sobrevivir cuando la infraestructura tradicional falla.






# Arquitectura Jerárquica de Nodos

# Idea principal

No todos los nodos deben hacer lo mismo.

La red funciona mejor cuando existen nodos especializados.

Esto permite:

- reducir congestión,
- ahorrar batería,
- mejorar escalabilidad,
- distribuir carga,
- estabilizar la red.

---

# Tipos de nodos

---

# 1. User Node

## Nodo usuario

Nodo básico utilizado por:

- civiles,
- brigadistas,
- rescatistas.

---

## Funciones

- enviar mensajes,
- compartir GPS,
- enviar alertas,
- conectarse a la red.

---

## Hardware típico

- ESP32,
- LoRa,
- batería pequeña.

---

## Características

- portátil,
- bajo consumo,
- funciones simples.

---

# 2. Relay Node

## Nodo retransmisor

Especializado en retransmitir tráfico.

---

## Funciones

- ampliar cobertura,
- conectar zonas,
- retransmitir paquetes.

---

## Características

- mejor antena,
- batería más grande,
- posición estratégica.

---

## Ubicaciones posibles

- cerros,
- postes,
- vehículos,
- drones,
- edificios.

---

# 3. Super Node

## Nodo coordinador

Nodo más potente de la red.

---

## Funciones

- manejar clusters,
- administrar rutas,
- controlar congestión,
- optimizar tráfico.

---

## Características

- mayor batería,
- mejor CPU,
- mejor señal,
- posición elevada.

---

## Funciones avanzadas

- mantener tablas de rutas,
- seleccionar mejores caminos,
- redistribuir tráfico,
- detectar congestión.

---

# 4. Sensor Node

## Nodo IoT

Especializado en monitoreo ambiental.

---

## Sensores posibles

- humo,
- temperatura,
- gas,
- vibración,
- humedad,
- movimiento.

---

## Función

Enviar telemetría automáticamente.

---

## Ejemplo

Sensor detecta incendio
↓
Genera alerta automática
↓
La red retransmite la alerta

---

# 5. Gateway Node

## Nodo puente

Conecta la red mesh con sistemas externos.

---

## Posibles conexiones

- internet,
- satélite,
- Starlink,
- fibra óptica,
- centros de emergencia.

---

## Función

- sincronizar información,
- conectar con servicios externos,
- exportar datos.

---

# 6. Command Node

## Nodo de comando

Centro de visualización y coordinación.

---

## Funciones

- visualizar mapas,
- monitorear nodos,
- ver alertas,
- coordinar brigadas.

---

## Información posible

- nodos activos,
- incendios,
- usuarios,
- telemetría,
- estado red.

---

# Super Nodos

Algunos nodos pueden convertirse automáticamente en nodos prioritarios.

---

# Criterios

| Condición | Resultado |
|---|---|
| batería alta | relay |
| buena señal | super nodo |
| energía permanente | nodo estable |
| posición elevada | nodo estratégico |

---

# Auto-organización

La red puede decidir automáticamente:

- qué nodo retransmite,
- qué nodo coordina,
- qué nodo conecta clusters.

---

# Hierarchical Mesh

En vez de una red plana:

Todos ↔ Todos

Se crea una estructura organizada:

Usuarios
↓
Relays
↓
Super Nodos
↓
Gateways

---

# Ventajas de arquitectura jerárquica

- mejor rendimiento,
- menos tráfico innecesario,
- mayor estabilidad,
- menor congestión,
- mejor escalabilidad,
- mejor administración energética.

---

# Ejemplo de despliegue en emergencia

## Incendio forestal

| Nodo | Función |
|---|---|
| drones | cobertura aérea |
| sensores | detectar humo |
| brigadistas | comunicación |
| vehículo comando | super nodo |
| gateway | conexión externa |

---

# Objetivo final

Crear una red distribuida inteligente capaz de:

- adaptarse automáticamente,
- reorganizarse dinámicamente,
- priorizar tráfico crítico,
- mantener comunicación estable incluso en desastres.





Cada nodo debe poder:

✅ existir solo
✅ operar solo
✅ enviar mensajes solo
✅ crear redes espontáneas
✅ tomar decisiones locales
✅ sobrevivir aislado

SIN necesitar:

❌ servidor central
❌ internet
❌ nube
❌ nodo maestro obligatorio
❌ comando permanente




# Sistema de Identidad y Funciones Dinámicas de los Nodos

# Idea principal

Cada nodo de la red mesh es:

- independiente,
- autónomo,
- descentralizado.

Pero además:

# cada nodo puede reconocer:
- quién es,
- qué puede hacer,
- y cuál es su ventaja estratégica actual.

---

# Filosofía del sistema

La red NO depende de:
- servidores,
- internet,
- nube,
- control central.

En cambio:

# la red emerge de la cooperación entre nodos.

Cada nodo:
- toma decisiones locales,
- comparte información,
- colabora dinámicamente.

---

# Dos conceptos fundamentales

| Concepto | Significado |
|---|---|
| identidad | qué representa el nodo |
| función dinámica | qué puede hacer actualmente |

---

# 1. Identidad del Nodo

La identidad representa:

# “quién soy”

Es relativamente estable.

---

# Ejemplos de identidad

| Código | Identidad |
|---|---|
| 0x01 | bombero |
| 0x02 | ambulancia |
| 0x03 | policía |
| 0x04 | médico |
| 0x05 | civil |
| 0x06 | dron |
| 0x07 | comando |

---

# Funciones de la identidad

La identidad ayuda a:

- priorizar mensajes,
- filtrar eventos,
- organizar equipos,
- definir protocolos,
- coordinar emergencias.

---

# Ejemplo

```json
{
  "id": "NODE_014",
  "identity": "FIREFIGHTER"
}
```

---

# 2. Funciones Dinámicas

Las funciones dinámicas representan:

# “qué puedo hacer ahora”

NO son permanentes.

Cambian según:
- batería,
- señal,
- posición,
- tráfico,
- sensores,
- energía disponible,
- cantidad de vecinos.

---

# Filosofía

El nodo NO recibe órdenes centrales.

El nodo:

# detecta sus ventajas estratégicas y decide colaborar.

---

# Ejemplo

Nodo detecta:

- batería alta,
- excelente señal,
- posición elevada.

Entonces:

```text
“puedo actuar como relay”
```

---

# Ejemplos de funciones dinámicas

| Función | Descripción |
|---|---|
| RELAY | retransmitir paquetes |
| SUPER_NODE | coordinar tráfico local |
| GATEWAY | conectar con internet/satélite |
| SENSOR_NODE | transmitir sensores |
| GPS_PROVIDER | compartir ubicación |
| STORAGE_NODE | almacenar mensajes temporalmente |
| COMMAND_SUPPORT | apoyar coordinación |

---

# Ejemplo completo

```json
{
  "id": "NODE_014",

  "identity": "FIREFIGHTER",

  "dynamic_functions": [
    "RELAY",
    "GPS_PROVIDER"
  ],

  "battery": 91,
  "neighbors": 14,
  "signal_quality": "HIGH"
}
```

---

# Ventajas estratégicas

Cada nodo analiza constantemente:

| Variable | Uso |
|---|---|
| batería | decidir retransmisión |
| señal | calidad enlace |
| altura | cobertura |
| vecinos | conectividad |
| tráfico | congestión |
| energía externa | estabilidad |
| sensores | capacidades |

---

# Ejemplo de decisiones autónomas

## Caso 1

Nodo detecta:
- energía estable,
- buena posición,
- muchos vecinos.

↓

Se convierte temporalmente en:

```text
SUPER_NODE
```

---

## Caso 2

Nodo tiene:
- poca batería,
- baja señal.

↓

Reduce:
- retransmisión,
- tráfico,
- prioridad técnica.

---

## Caso 3

Nodo dron detecta:
- altura elevada,
- gran cobertura.

↓

Asume función:

```text
AERIAL_RELAY
```

---

# Roles técnicos NO son permanentes

MUY importante.

Un nodo puede:
- ganar funciones,
- perder funciones,
- cambiar comportamiento.

---

# Ejemplo

Nodo actúa como relay durante:
- batería alta,
- buena cobertura.

Pero luego:
- baja batería,
- pierde altura.

↓

Deja automáticamente el rol relay.

---

# Auto-organización

La red NO tiene:
- jefe absoluto,
- servidor maestro.

En cambio:

# los nodos cooperan localmente.

---

# Filosofía distribuida

La inteligencia NO existe en un punto central.

La inteligencia:

# emerge del comportamiento colectivo.

---

# Comportamiento emergente

Ejemplo:

Muchos nodos detectan congestión.

↓

Algunos automáticamente:
- retransmiten menos,
- bajan prioridad,
- se convierten en relay,
- reorganizan rutas.

---

# Resultado

La red:
- se adapta sola,
- se reorganiza sola,
- sobrevive sola.

---

# Cooperación autónoma

Los nodos:
- NO obedecen,
- NO dependen,
- NO esperan instrucciones.

Los nodos:

# colaboran voluntariamente según sus capacidades.

---

# Ejemplo conceptual

## Nodo A

- mejor batería,
- mejor señal.

↓

Decide retransmitir más.

---

## Nodo B

- batería baja.

↓

Decide retransmitir menos.

---

# Resultado

La red se balancea automáticamente.

---

# Separación conceptual importante

| Tipo | Pregunta |
|---|---|
| identidad | quién soy |
| función dinámica | qué puedo hacer ahora |

---

# Ejemplo final

```json
{
  "id": "NODE_031",

  "identity": "MEDIC",

  "dynamic_functions": [
    "RELAY",
    "MEDICAL_PRIORITY",
    "GPS_PROVIDER"
  ],

  "battery": 88,
  "signal_strength": "HIGH",
  "neighbors": 9
}
```

---

# Resultado final del sistema

La red se vuelve:

- descentralizada,
- resiliente,
- adaptable,
- autónoma,
- auto-organizable,
- independiente,
- dinámica.

---

# Conceptos técnicos involucrados

- Mesh Networking
- Self-Organizing Networks
- Distributed Systems
- Swarm Intelligence
- Adaptive Routing
- Edge Intelligence
- Distributed Consensus
- Emergent Behavior
- Decentralized Communication
- Dynamic Role Assignment

---

# Visión final

Crear una red mesh autónoma donde:

- cada nodo es independiente,
- cada nodo coopera localmente,
- los roles emergen dinámicamente,
- las funciones cambian según contexto,
- y la red completa se adapta automáticamente a las condiciones del entorno.


LoRa, protocolo de comunicaion a usar