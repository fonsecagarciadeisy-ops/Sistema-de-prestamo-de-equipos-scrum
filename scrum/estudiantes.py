
from archivos import cargar_datos, guardar_datos, RUTA_ESTUDIANTES


def validar_documento(documento):
    if len(documento) == 0:
        return False
    return documento.isdigit()


def validar_nombre(nombre):
    texto = nombre.strip()
    if len(texto) == 0:
        return False
    for caracter in texto:
        if not caracter.isalpha() and caracter != " ":
            return False
    return True


def validar_telefono(telefono):
    if len(telefono) == 0:
        return False
    return telefono.isdigit()



def registrar_estudiante():
    """
    Registra un nuevo estudiante en el sistema.
    Pide documento, nombre y teléfono, los valida y los guarda.
    No recibe parámetros ni retorna nada.
    """
    print("\n========== REGISTRAR ESTUDIANTE ==========")

    # Pedir y validar el documento
    documento = input("Documento: ")
    while not validar_documento(documento):
        print(" El documento solo puede contener números.")
        documento = input("Documento: ")

    # Cargar estudiantes actuales
    estudiantes = cargar_datos(RUTA_ESTUDIANTES)

    # Verificar que no exista ya
    for estudiante in estudiantes:
        if estudiante["documento"] == documento:
            print(" El estudiante ya existe.")
            return

    # Pedir y validar el nombre
    nombre = input("Nombre completo: ")
    while not validar_nombre(nombre):
        print(" El nombre solo puede contener letras y espacios.")
        nombre = input("Nombre completo: ")

    # Pedir y validar el teléfono
    telefono = input("Teléfono: ")
    while not validar_telefono(telefono):
        print(" El teléfono solo puede contener números.")
        telefono = input("Teléfono: ")

    # Crear el diccionario del nuevo estudiante
    nuevo_estudiante = {
        "documento": documento,
        "nombre": nombre,
        "telefono": telefono
    }

    # Agregar a la lista y guardar
    estudiantes.append(nuevo_estudiante)
    guardar_datos(RUTA_ESTUDIANTES, estudiantes)

    print("Estudiante registrado correctamente.")


# ==============================
# MOSTRAR ESTUDIANTES
# ==============================

def mostrar_estudiantes():
    """
    Muestra en pantalla todos los estudiantes registrados.
    No recibe parámetros ni retorna nada.
    """
    print("\n========== LISTA DE ESTUDIANTES ==========")

    estudiantes = cargar_datos(RUTA_ESTUDIANTES)

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for estudiante in estudiantes:
        print("----------------------------------")
        print(f"Documento : {estudiante['documento']}")
        print(f"Nombre    : {estudiante['nombre']}")
        print(f"Teléfono  : {estudiante['telefono']}")



def buscar_estudiante():
    print("\n========== BUSCAR ESTUDIANTE ==========")

    documento = input("Documento del estudiante: ")

    estudiantes = cargar_datos(RUTA_ESTUDIANTES)

    for estudiante in estudiantes:
        if estudiante["documento"] == documento:
            print("\nEstudiante encontrado:")
            print(f"Documento : {estudiante['documento']}")
            print(f"Nombre    : {estudiante['nombre']}")
            print(f"Teléfono  : {estudiante['telefono']}")
            return

    print("Estudiante no encontrado.")
