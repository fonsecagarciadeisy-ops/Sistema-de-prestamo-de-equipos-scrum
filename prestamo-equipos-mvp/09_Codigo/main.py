"""
Sistema de Préstamo de Equipos Tecnológicos - MVP
=================================================

Aplicación de consola que gestiona el registro y la consulta de equipos
tecnológicos y el registro de estudiantes.

Alcance de este incremento (Sprint 1):
    HU01 - Registrar equipos tecnológicos.
    HU02 - Consultar los equipos registrados y su disponibilidad.
    HU03 - Registrar estudiantes.

Punto de entrada del programa: muestra el menú principal y coordina los
módulos equipos y estudiantes.

Ejecución:
    python main.py

Autores: Equipo Scrum - Sistema de Préstamo de Equipos Tecnológicos
"""

import equipos
import estudiantes
import utilidades as ui


# --------------------------------------------------------------------------- #
# Funciones de presentación (dan formato a la salida por consola)
# --------------------------------------------------------------------------- #

def mostrar_tabla_equipos(lista):
    """Imprime una tabla con los equipos recibidos."""
    if not lista:
        print("  (No hay equipos para mostrar.)")
        return
    print(f"  {'CÓDIGO':<10}{'TIPO':<15}{'MARCA':<15}{'MODELO':<20}{'ESTADO':<12}")
    print("  " + "-" * 72)
    for e in lista:
        print(f"  {e['codigo']:<10}{e['tipo']:<15}{e['marca']:<15}"
              f"{e['modelo']:<20}{e['estado']:<12}")


def mostrar_tabla_estudiantes(lista):
    """Imprime una tabla con los estudiantes recibidos."""
    if not lista:
        print("  (No hay estudiantes registrados.)")
        return
    print(f"  {'DOCUMENTO':<15}{'NOMBRE':<25}{'CORREO':<28}{'PROGRAMA':<25}")
    print("  " + "-" * 93)
    for e in lista:
        print(f"  {e['documento']:<15}{e['nombre']:<25}{e['correo']:<28}"
              f"{e['programa']:<25}")


# --------------------------------------------------------------------------- #
# Opciones del menú (cada una corresponde a una historia de usuario)
# --------------------------------------------------------------------------- #

def opcion_registrar_equipo():
    """HU01 - Registrar un equipo tecnológico."""
    ui.titulo("Registrar equipo (HU01)")
    codigo = ui.leer_texto("  Código del equipo: ")
    tipo = ui.leer_texto("  Tipo (portátil, tablet, proyector...): ")
    marca = ui.leer_texto("  Marca: ")
    modelo = ui.leer_texto("  Modelo: ")
    try:
        equipo = equipos.registrar_equipo(codigo, tipo, marca, modelo)
        print(f"\n  Equipo '{equipo['codigo']}' registrado correctamente.")
    except ValueError as error:
        print(f"\n  Error: {error}")


def opcion_listar_equipos():
    """HU02 - Consultar los equipos registrados y su disponibilidad."""
    ui.titulo("Inventario de equipos (HU02)")
    mostrar_tabla_equipos(equipos.listar_equipos())


def opcion_registrar_estudiante():
    """HU03 - Registrar un estudiante."""
    ui.titulo("Registrar estudiante (HU03)")
    documento = ui.leer_texto("  Documento: ")
    nombre = ui.leer_texto("  Nombre completo: ")
    correo = ui.leer_correo("  Correo: ")
    programa = ui.leer_texto("  Programa académico: ")
    try:
        estudiante = estudiantes.registrar_estudiante(
            documento, nombre, correo, programa)
        print(f"\n  Estudiante '{estudiante['nombre']}' registrado correctamente.")
    except ValueError as error:
        print(f"\n  Error: {error}")


def opcion_listar_estudiantes():
    """Consultar los estudiantes registrados (apoyo a HU03)."""
    ui.titulo("Estudiantes registrados")
    mostrar_tabla_estudiantes(estudiantes.listar_estudiantes())


# --------------------------------------------------------------------------- #
# Menú principal
# --------------------------------------------------------------------------- #

# Mapa: opción del menú -> (texto, función a ejecutar)
OPCIONES = {
    "1": ("Registrar equipo (HU01)", opcion_registrar_equipo),
    "2": ("Listar equipos (HU02)", opcion_listar_equipos),
    "3": ("Registrar estudiante (HU03)", opcion_registrar_estudiante),
    "4": ("Listar estudiantes", opcion_listar_estudiantes),
}


def mostrar_menu():
    """Imprime el menú principal con todas las opciones disponibles."""
    ui.titulo("SISTEMA DE PRÉSTAMO DE EQUIPOS TECNOLÓGICOS")
    for clave in sorted(OPCIONES):
        texto = OPCIONES[clave][0]
        print(f"  {clave}. {texto}")
    print("  0. Salir")


def main():
    """Bucle principal del programa."""
    print("\nBienvenido al Sistema de Préstamo de Equipos Tecnológicos (MVP)")
    while True:
        mostrar_menu()
        opcion = ui.leer_opcion("\n  Seleccione una opción: ",
                                set(OPCIONES) | {"0"})
        if opcion == "0":
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break

        _, accion = OPCIONES[opcion]
        accion()
        ui.pausar()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. ¡Hasta pronto!")
