# Sistema de Gestión de Préstamo de Equipos

Sistema de consola en Python para gestionar el préstamo de equipos tecnológicos a estudiantes. Permite registrar estudiantes, registrar equipos, realizar préstamos y devoluciones, y consultar el historial.

## Estructura del Proyecto

```
proyecto/
├── main.py              # Menú principal del programa
├── archivos.py          # Funciones para leer y guardar archivos JSON
├── estudiantes.py       # Funciones para gestionar estudiantes
├── equipos.py           # Funciones para gestionar equipos
├── prestamos.py         # Funciones para gestionar préstamos
├── README.md            # Este archivo
└── datos/
    ├── estudiantes.json # Datos de los estudiantes registrados
    ├── equipos.json     # Datos de los equipos registrados
    └── prestamos.json   # Datos de los préstamos realizados
```

## Qué hace cada módulo

### `main.py`
Contiene el menú principal del programa. Muestra las opciones al usuario y llama a las funciones de los otros módulos según la opción elegida.

### `archivos.py`
Contiene dos funciones para trabajar con archivos JSON:
- `cargar_datos(ruta)` — Lee un archivo JSON y devuelve su contenido como lista
- `guardar_datos(ruta, datos)` — Guarda una lista en un archivo JSON

También define las rutas a los tres archivos de datos (`RUTA_ESTUDIANTES`, `RUTA_EQUIPOS`, `RUTA_PRESTAMOS`).

### `estudiantes.py`
Funciones para gestionar estudiantes:
- `registrar_estudiante()` — Registra un nuevo estudiante con documento, nombre y teléfono
- `mostrar_estudiantes()` — Muestra la lista de todos los estudiantes
- `buscar_estudiante()` — Busca un estudiante por su número de documento

### `equipos.py`
Funciones para gestionar equipos:
- `registrar_equipo()` — Registra un nuevo equipo con código, nombre, tipo y marca
- `mostrar_equipos()` — Muestra la lista de todos los equipos con su estado
- `buscar_equipo()` — Busca un equipo por su código

### `prestamos.py`
Funciones para gestionar préstamos:
- `prestar_equipo()` — Registra el préstamo de un equipo a un estudiante
- `devolver_equipo()` — Registra la devolución de un equipo prestado
- `mostrar_historial()` — Muestra el historial completo de préstamos

## Estructura de datos JSON

### `datos/estudiantes.json`
```json
[
    {
        "documento": "15456656",
        "nombre": "Santiago jimenez",
        "telefono": "356644856"
    }
]
```
| Campo      | Tipo   | Descripción                          |
|------------|--------|--------------------------------------|
| documento  | texto  | Número de documento del estudiante   |
| nombre     | texto  | Nombre completo del estudiante       |
| telefono   | texto  | Número de teléfono del estudiante    |

### `datos/equipos.json`
```json
[
    {
        "codigo": "DH-54665",
        "nombre": "DELL",
        "tipo": "PORTATIL",
        "marca": "DELL LATITUDE",
        "estado": "Disponible"
    }
]
```
| Campo   | Tipo   | Descripción                                    |
|---------|--------|------------------------------------------------|
| codigo  | texto  | Código único del equipo                        |
| nombre  | texto  | Nombre del equipo                              |
| tipo    | texto  | Tipo de equipo (Portátil, Tablet, etc.)        |
| marca   | texto  | Marca del equipo                               |
| estado  | texto  | Estado actual: "Disponible" o "Prestado"       |

### `datos/prestamos.json`
```json
[
    {
        "documento": "15456656",
        "usuario": "Santiago jimenez",
        "codigo_equipo": "DH-54665",
        "equipo": "DELL",
        "fecha_prestamo": "2026-08-26 16:45:17",
        "fecha_devolucion": null,
        "estado": "Activo"
    }
]
```
| Campo            | Tipo       | Descripción                                  |
|------------------|------------|----------------------------------------------|
| documento        | texto      | Documento del estudiante que pidió prestado   |
| usuario          | texto      | Nombre del estudiante                        |
| codigo_equipo    | texto      | Código del equipo prestado                   |
| equipo           | texto      | Nombre del equipo prestado                   |
| fecha_prestamo   | texto      | Fecha y hora del préstamo                    |
| fecha_devolucion | texto/null | Fecha de devolución (null si no se ha devuelto) |
| estado           | texto      | Estado: "Activo" o "Devuelto"                |

## Cómo ejecutar el proyecto

### Requisitos
- Python 3.6 o superior
- No se necesitan librerías externas

### Ejecución
```bash
python main.py
```

El programa mostrará un menú con las opciones disponibles. Escriba el número de la opción y presione Enter.
