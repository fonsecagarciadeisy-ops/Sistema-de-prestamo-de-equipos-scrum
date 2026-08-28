"""
Módulo de utilidades.

Funciones auxiliares para leer datos por consola de forma segura (con
validación) y para dar formato a la salida. Separar esto del resto del código
evita repetir validaciones y mantiene los módulos de negocio más limpios.
"""

import re

# Expresión regular sencilla para validar un correo con forma 'algo@algo.algo'.
PATRON_CORREO = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def leer_texto(mensaje, obligatorio=True):
    """
    Lee texto por consola.

    Si 'obligatorio' es True, no acepta cadenas vacías y vuelve a preguntar.
    Elimina espacios sobrantes al inicio y al final.
    """
    while True:
        valor = input(mensaje).strip()
        if valor or not obligatorio:
            return valor
        print("  * Este campo es obligatorio. Intente nuevamente.")


def leer_correo(mensaje):
    """Lee un correo electrónico y valida que tenga un formato razonable."""
    while True:
        correo = input(mensaje).strip()
        if PATRON_CORREO.match(correo):
            return correo
        print("  * Correo no válido. Ejemplo: nombre@dominio.com")


def leer_opcion(mensaje, opciones_validas):
    """
    Lee una opción de menú y valida que pertenezca al conjunto permitido.

    'opciones_validas' es una colección de cadenas, por ejemplo {'0','1','2'}.
    """
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print("  * Opción no válida. Intente nuevamente.")


def titulo(texto):
    """Imprime un título con una línea separadora, para dar formato al menú."""
    print()
    print("=" * 55)
    print(f" {texto}")
    print("=" * 55)


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")
