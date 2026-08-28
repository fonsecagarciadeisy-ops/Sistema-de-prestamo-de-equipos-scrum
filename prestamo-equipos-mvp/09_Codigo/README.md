# Sistema de Préstamo de Equipos Tecnológicos — MVP

Aplicación de consola en **Python** que permite a una institución educativa
gestionar el préstamo y la devolución de equipos tecnológicos (portátiles,
tablets, proyectores, etc.) a sus estudiantes.

Este es el **incremento funcional** desarrollado durante el Sprint 1 aplicando
Scrum. Su alcance son las tres primeras historias: **registrar equipos (HU01)**,
**consultar equipos (HU02)** y **registrar estudiantes (HU03)**. La gestión de
préstamos y devoluciones queda planificada para un Sprint posterior.

---

## Requisitos

- **Python 3.8 o superior** (no requiere librerías externas; solo la librería
  estándar).

Comprobar la versión instalada:

```bash
python --version
```

> En Windows, si `python` no funciona, prueba con `py`.

---

## Instalación y ejecución

1. Clona o descarga el repositorio.
2. Entra en la carpeta del código:

```bash
cd 09_Codigo
```

3. Ejecuta la aplicación:

```bash
python main.py
```

(o `py main.py` en Windows).

No hay que instalar dependencias: el proyecto usa únicamente módulos de la
librería estándar de Python (`json`, `os`, `re`, `datetime`).

---

## Estructura del proyecto

```
09_Codigo/
├── main.py          # Punto de entrada: menú principal e interacción por consola
├── equipos.py       # Alta y consulta de equipos (HU01, HU02)
├── estudiantes.py   # Alta y consulta de estudiantes (HU03)
├── archivos.py      # Persistencia: lectura/escritura de los archivos JSON
├── utilidades.py    # Lectura validada por consola y formato de salida
├── tests/
│   └── test_sistema.py   # Pruebas automatizadas (unittest)
└── datos/
    ├── equipos.json      # Inventario de equipos
    └── estudiantes.json  # Estudiantes registrados
```

La aplicación **guarda los datos automáticamente** en los archivos JSON de la
carpeta `datos/`, de modo que la información persiste entre ejecuciones.

---

## Funcionalidades (menú)

| Opción | Funcionalidad                        | Historia |
|:------:|--------------------------------------|:--------:|
| 1      | Registrar equipo                     | HU01     |
| 2      | Listar equipos y disponibilidad      | HU02     |
| 3      | Registrar estudiante                 | HU03     |
| 4      | Listar estudiantes                   | (apoyo)  |
| 0      | Salir                                |          |

### Reglas de negocio validadas

- No se permiten **códigos de equipo** ni **documentos de estudiante** duplicados.
- Cada equipo se registra con estado inicial `disponible`.
- El **correo** del estudiante se valida con formato `nombre@dominio.com`.
- Los campos obligatorios no aceptan valores vacíos.

---

## Pruebas

El proyecto incluye pruebas automatizadas con `unittest`. Para ejecutarlas,
desde la carpeta `09_Codigo`:

```bash
python -m unittest discover -s tests -v
```

Las pruebas usan una carpeta de datos temporal, por lo que **no modifican** los
archivos JSON reales.

---

## Modelo de datos (JSON)

**Equipo**

```json
{ "codigo": "EQ001", "tipo": "Portátil", "marca": "Lenovo",
  "modelo": "ThinkPad E14", "estado": "disponible" }
```

**Estudiante**

```json
{ "documento": "1001234567", "nombre": "Ana Pérez",
  "correo": "ana.perez@campus.edu", "programa": "Ingeniería de Sistemas" }
```
