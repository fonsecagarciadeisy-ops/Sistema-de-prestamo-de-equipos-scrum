"""
Módulo de equipos.

Gestiona el inventario de equipos tecnológicos: registro (HU01) y consulta
(HU02). Cada equipo es un diccionario con la siguiente forma:

    {
        "codigo": "EQ001",
        "tipo": "Portátil",
        "marca": "Lenovo",
        "modelo": "ThinkPad E14",
        "estado": "disponible"
    }
"""

from archivos import cargar, guardar, ARCHIVO_EQUIPOS

# Estado inicial de un equipo al registrarlo.
ESTADO_DISPONIBLE = "disponible"


def _cargar():
    """Carga la lista de equipos desde el archivo JSON."""
    return cargar(ARCHIVO_EQUIPOS)


def _guardar(equipos):
    """Guarda la lista de equipos en el archivo JSON."""
    guardar(ARCHIVO_EQUIPOS, equipos)


def registrar_equipo(codigo, tipo, marca, modelo):
    """
    Registra un nuevo equipo en el inventario (HU01).

    Valida que el código no esté repetido. Lanza ValueError si ya existe.
    Devuelve el equipo registrado.
    """
    equipos = _cargar()
    if any(e["codigo"].lower() == codigo.strip().lower() for e in equipos):
        raise ValueError(f"Ya existe un equipo con el código '{codigo}'.")

    equipo = {
        "codigo": codigo.strip(),
        "tipo": tipo.strip(),
        "marca": marca.strip(),
        "modelo": modelo.strip(),
        "estado": ESTADO_DISPONIBLE,
    }
    equipos.append(equipo)
    _guardar(equipos)
    return equipo


def listar_equipos():
    """Devuelve la lista completa de equipos y su disponibilidad (HU02)."""
    return _cargar()
