"""
Módulo de persistencia.

Centraliza la lectura y escritura de los datos del sistema en archivos JSON.
Todos los demás módulos (equipos, estudiantes, préstamos) usan estas funciones
para no repetir la lógica de acceso a disco.
"""

import json
import os

# Carpeta 'datos/' ubicada junto a este archivo, independientemente de desde
# dónde se ejecute el programa.
CARPETA_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos")

# Nombres de los archivos de datos (una "tabla" por archivo).
ARCHIVO_EQUIPOS = "equipos.json"
ARCHIVO_ESTUDIANTES = "estudiantes.json"


def _ruta(nombre_archivo):
    """Devuelve la ruta absoluta de un archivo dentro de la carpeta de datos."""
    return os.path.join(CARPETA_DATOS, nombre_archivo)


def cargar(nombre_archivo):
    """
    Carga una lista de registros desde un archivo JSON.

    Devuelve una lista vacía si el archivo no existe todavía o si su contenido
    está dañado, de modo que el programa nunca se detenga por un problema de
    lectura.
    """
    ruta = _ruta(nombre_archivo)
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            # Aseguramos que siempre trabajemos con una lista.
            return datos if isinstance(datos, list) else []
    except (json.JSONDecodeError, OSError):
        print(f"  [Advertencia] No se pudo leer '{nombre_archivo}'. "
              f"Se usará una lista vacía.")
        return []


def guardar(nombre_archivo, datos):
    """
    Guarda una lista de registros en un archivo JSON.

    Crea la carpeta 'datos/' si aún no existe. Usa indentación y
    ensure_ascii=False para que el archivo sea legible (incluye tildes y ñ).
    """
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    ruta = _ruta(nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)
