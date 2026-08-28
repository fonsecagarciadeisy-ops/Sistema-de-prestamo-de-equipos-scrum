
from datetime import datetime
from archivos import cargar_datos, guardar_datos
from archivos import RUTA_ESTUDIANTES, RUTA_EQUIPOS, RUTA_PRESTAMOS



def prestar_equipo():
    """
    Registra un préstamo de equipo a un estudiante.
    Verifica que el estudiante y el equipo existan,
    y que el equipo esté disponible.
    No recibe parámetros ni retorna nada.
    """
    print("\n========== PRÉSTAMO DE EQUIPO ==========")
    
    documento = input("Documento del estudiante: ")

    estudiantes = cargar_datos(RUTA_ESTUDIANTES)
    estudiante_encontrado = None

    for estudiante in estudiantes:
        if estudiante["documento"] == documento:
            estudiante_encontrado = estudiante
            break

    if estudiante_encontrado is None:
        print("Estudiante no encontrado.")
        return

    codigo = input("Código del equipo: ")

    equipos = cargar_datos(RUTA_EQUIPOS)
    equipo_encontrado = None

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            equipo_encontrado = equipo
            break

    if equipo_encontrado is None:
        print("Equipo no encontrado.")
        return

    
    if equipo_encontrado["estado"] != "Disponible":
        print("El equipo no está disponible.")
        return

    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nuevo_prestamo = {
        "documento": documento,
        "usuario": estudiante_encontrado["nombre"],
        "codigo_equipo": codigo,
        "equipo": equipo_encontrado["nombre"],
        "fecha_prestamo": fecha,
        "fecha_devolucion": None,
        "estado": "Activo"
    }

    
    prestamos = cargar_datos(RUTA_PRESTAMOS)
    prestamos.append(nuevo_prestamo)
    guardar_datos(RUTA_PRESTAMOS, prestamos)

    
    equipo_encontrado["estado"] = "Prestado"
    guardar_datos(RUTA_EQUIPOS, equipos)

    print("\nPRÉSTAMO REALIZADO")
    print(f"Estudiante: {estudiante_encontrado['nombre']}")
    print(f"Equipo: {equipo_encontrado['nombre']}")
    print(f"Fecha: {fecha}")



def devolver_equipo():
    """
    Registra la devolución de un equipo prestado.
    Busca el préstamo activo por código de equipo.
    No recibe parámetros ni retorna nada.
    """
    print("\n========== DEVOLVER EQUIPO ==========")

    codigo = input("Código del equipo: ")

    prestamos = cargar_datos(RUTA_PRESTAMOS)
    prestamo_encontrado = None

    for prestamo in prestamos:
        if prestamo["codigo_equipo"] == codigo and prestamo["estado"] == "Activo":
            prestamo_encontrado = prestamo
            break

    if prestamo_encontrado is None:
        print(" No existe un préstamo activo para ese equipo.")
        return

    
    equipos = cargar_datos(RUTA_EQUIPOS)

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            equipo["estado"] = "Disponible"
            break

    guardar_datos(RUTA_EQUIPOS, equipos)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prestamo_encontrado["fecha_devolucion"] = fecha
    prestamo_encontrado["estado"] = "Devuelto"
    guardar_datos(RUTA_PRESTAMOS, prestamos)

    print("Equipo devuelto correctamente.")
    print(f"Fecha de devolución: {fecha}")

def mostrar_historial():
    """
    Muestra en pantalla todos los préstamos registrados.
    No recibe parámetros ni retorna nada.
    """
    print("\n========== HISTORIAL DE PRÉSTAMOS ==========")

    prestamos = cargar_datos(RUTA_PRESTAMOS)

    if len(prestamos) == 0:
        print("No hay préstamos registrados.")
        return

    for prestamo in prestamos:
        print("----------------------------------")
        print(f"Estudiante : {prestamo['usuario']}")
        print(f"Documento  : {prestamo['documento']}")
        print(f"Equipo     : {prestamo['equipo']}")
        print(f"Código     : {prestamo['codigo_equipo']}")
        print(f"Préstamo   : {prestamo['fecha_prestamo']}")

        if prestamo["fecha_devolucion"] is None:
            print("Devolución : Pendiente")
        else:
            print(f"Devolución : {prestamo['fecha_devolucion']}")

        print(f"Estado     : {prestamo['estado']}")
    
