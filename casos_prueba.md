# Casos de Prueba — Sistema de Préstamo de Equipos Tecnológicos

Casos de prueba diseñados a partir de los criterios de aceptación de las
historias de usuario del Sprint 1 (HU01–HU03). Incluyen pruebas de **caminos
válidos** y de **validación de errores**.

| ID | Historia | Descripción | Datos de entrada | Resultado esperado | Resultado | Estado |
|----|:--------:|-------------|------------------|--------------------|-----------|:------:|
| CP-01 | HU01 | Registrar un equipo nuevo | EQ001 / Portátil / Lenovo / E14 | Equipo creado con estado `disponible` | Igual | OK |
| CP-02 | HU01 | No permitir código duplicado | EQ001 repetido | Error: "Ya existe un equipo con el código EQ001" | Igual | OK |
| CP-03 | HU01 | Rechazar campo obligatorio vacío | código vacío | Solicita de nuevo el dato | Igual | OK |
| CP-04 | HU02 | Listar equipos con datos | — | Se muestran los equipos con su estado | Igual | OK |
| CP-05 | HU02 | Listar equipos sin datos | — | Mensaje "(No hay equipos para mostrar.)" | Igual | OK |
| CP-06 | HU03 | Registrar estudiante | 100 / Ana / ana@campus.edu / Sistemas | Estudiante creado | Igual | OK |
| CP-07 | HU03 | No permitir documento duplicado | Documento 100 repetido | Error: "Ya existe un estudiante..." | Igual | OK |
| CP-08 | HU03 | Rechazar correo inválido | correo "ana@" | Solicita de nuevo el correo | Igual | OK |

---

## Cobertura por pruebas automatizadas

Los casos CP-01, CP-02, CP-05, CP-06 y CP-07 están cubiertos por pruebas
automatizadas en
[`09_Codigo/tests/test_sistema.py`](../09_Codigo/tests/test_sistema.py).

Los casos CP-03, CP-04 y CP-08 se verifican manualmente por consola (evidencia
en video / capturas de la Sprint Review).
