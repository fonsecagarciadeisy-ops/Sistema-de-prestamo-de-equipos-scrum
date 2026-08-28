"""
Módulo de estudiantes.

Gestiona el registro y la consulta de estudiantes. Cada estudiante es un
diccionario con la forma:

    {
        "documento": "1001234567",
        "nombre": "Ana Pérez",
        "correo": "ana.perez@campus.edu",
        "programa": "Ingeniería de Sistemas"
    }
"""

from archivos import cargar, guardar, ARCHIVO_ESTUDIANTES


def _cargar():
    """Carga la lista de estudiantes desde el archivo JSON."""
    return cargar(ARCHIVO_ESTUDIANTES)


def _guardar(estudiantes):
    """Guarda la lista de estudiantes en el archivo JSON."""
    guardar(ARCHIVO_ESTUDIANTES, estudiantes)


def buscar_estudiante(documento):
    """
    Busca un estudiante por su documento.

    Devuelve el diccionario del estudiante o None si no existe.
    """
    documento = documento.strip()
    for estudiante in _cargar():
        if estudiante["documento"] == documento:
            return estudiante
    return None


def registrar_estudiante(documento, nombre, correo, programa):
    """
    Registra un nuevo estudiante (HU03).

    Valida que el documento no esté repetido. Lanza ValueError si ya existe.
    Devuelve el estudiante registrado.
    """
    estudiantes = _cargar()
    if any(e["documento"] == documento.strip() for e in estudiantes):
        raise ValueError(f"Ya existe un estudiante con el documento '{documento}'.")

    estudiante = {
        "documento": documento.strip(),
        "nombre": nombre.strip(),
        "correo": correo.strip(),
        "programa": programa.strip(),
    }
    estudiantes.append(estudiante)
    _guardar(estudiantes)
    return estudiante


def listar_estudiantes():
    """Devuelve la lista completa de estudiantes."""
    return _cargar()
