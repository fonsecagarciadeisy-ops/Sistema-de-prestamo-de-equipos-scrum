# Product Backlog — Sistema de Préstamo de Equipos Tecnológicos

**Product Owner:** *[deisy katerinne]*
**Fecha de elaboración:** *[25/08/26]*

El Product Backlog es la lista ordenada y priorizada de todo lo que el producto
necesita. Cada historia incluye prioridad, estimación en **Story Points (SP)** y
**criterios de aceptación**.

---

## Historias de usuario

### HU01 — Registrar equipos tecnológicos · Prioridad: Alta · 3 SP
> Como administrador, quiero registrar equipos tecnológicos para mantener
> actualizado el inventario.

**Criterios de aceptación**
- Se solicitan código, tipo, marca y modelo.
- El equipo se guarda con estado inicial `disponible`.
- No se permite registrar dos equipos con el mismo código.
- Los campos obligatorios no pueden quedar vacíos.

---

### HU02 — Consultar equipos registrados · Prioridad: Alta · 2 SP
> Como administrador, quiero consultar los equipos registrados para conocer su
> disponibilidad.

**Criterios de aceptación**
- Se listan todos los equipos con código, tipo, marca, modelo y estado.
- Se muestra la disponibilidad de cada equipo.
- Si no hay equipos, se muestra un mensaje informativo.

---

### HU03 — Registrar estudiantes · Prioridad: Alta · 3 SP
> Como administrador, quiero registrar estudiantes para asociarlos a los
> préstamos.

**Criterios de aceptación**

- Se solicitan documento, nombre, correo y programa académico.
- El correo se valida con formato `nombre@dominio.com`.
- No se permite registrar dos estudiantes con el mismo documento.

---

## Resumen y priorización

| ID   | Historia                          | Prioridad | SP | Estado    |
|------|-----------------------------------|:---------:|:--:|-----------|
| HU01 | Registrar equipos                 | Alta      | 3 | Done   |
| HU02 | Consultar equipos                 | Alta      | 2  | Done   |
| HU03 | Registrar estudiantes             | Alta      | 3  | Done   |
|      | **Total**                         |           | **8** |       |
