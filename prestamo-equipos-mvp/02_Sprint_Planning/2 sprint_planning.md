# Acta de Sprint Planning

| Campo | Detalle |
|-------|---------|
| **Fecha** | *[25/08/26]* |
| **Asistentes** | *[Product Owner, Scrum Master, Developers]* |
| **Sprint** | Sprint 1 (1 semana) |
| **Duración del Sprint** | *[25/07/26]* — *[25/07/26]* |

---

## 1. Sprint Goal (Objetivo del Sprint)

> Entregar un **MVP de consola en Python** que permita **registrar equipos**
> tecnológicos, **consultar el inventario** y su disponibilidad, y **registrar
> estudiantes**, con **persistencia de datos en archivos JSON**. Esta es la base,
> sobre la que se construirá el proceso de préstamo y devolución en Sprints
> posteriores.

---

## 2. Historias seleccionadas para el Sprint

Se seleccionan las tres primeras historias del Product Backlog, todas de
prioridad Alta, que conforman el núcleo de datos del sistema.

| ID   | Historia                        | Prioridad | SP |
|------|---------------------------------|:---------:|:--:|
| HU01 | Registrar equipos               | Alta      | 3  |
| HU02 | Consultar equipos               | Alta      | 2  |
| HU03 | Registrar estudiantes           | Alta      | 3  |
|      | **Total comprometido**          |           | **8** |

---

## 3. Sprint Backlog (historias → tareas técnicas)

| Historia | Tareas técnicas | Responsable |
|----------|-----------------|-------------|
| Infra    | Crear estructura modular del proyecto y módulo de persistencia `archivos.py` | Dev |
| Infra    | Crear utilidades de entrada validada y formato (`utilidades.py`) | *Dev* |
| HU01     | Función `registrar_equipo` + validación de código único | Dev |
| HU02     | Función `listar_equipos` + tabla de salida | Dev |
| HU03     | Función `registrar_estudiante` + validación de correo y documento único | Dev |
| Calidad  | Pruebas automatizadas (`tests/test_sistema.py`) | *Dev* |
| Docs     | README, informe y evidencias | Dev |

---

## 4. Definición de Terminado (Definition of Done)

Una historia se considera **Done** cuando:

- [x] La funcionalidad cumple **todos** sus criterios de aceptación.
- [x] El código está integrado en el repositorio (con commit).
- [x] Tiene validación de datos y manejo de errores básicos
- [x] Está cubierta por al menos una prueba (cuando aplica).
- [x] Fue verificada manualmente por consola.

---

## 5. Capacidad y acuerdos

- **Capacidad comprometida:** 8 Story Points.
- **Acuerdos del equipo:** Daily Scrum diario de 10–15 min; el código se integra
  con commits pequeños y descriptivos; los impedimentos se registran en
  `04_Impedimentos/`
- **Evidencia:** 
