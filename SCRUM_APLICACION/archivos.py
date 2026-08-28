
import json
import os



CARPETA_BASE = os.path.dirname(os.path.abspath(__file__))


RUTA_ESTUDIANTES = os.path.join(CARPETA_BASE, "datos", "estudiantes.json")
RUTA_EQUIPOS = os.path.join(CARPETA_BASE, "datos", "equipos.json")
RUTA_PRESTAMOS = os.path.join(CARPETA_BASE, "datos", "prestamos.json")




def cargar_datos(ruta_archivo):
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos
        else:
            return []
    except Exception:
        print(f"Error al leer el archivo: {ruta_archivo}")
        return []


def guardar_datos(ruta_archivo, datos):
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception:
        print(f"Error al guardar el archivo: {ruta_archivo}")
        return False
