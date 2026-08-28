
from archivos import cargar_datos, guardar_datos, RUTA_EQUIPOS




def validar_codigo(codigo):
    if len(codigo) == 0:
        return False

    for caracter in codigo:
        if not caracter.isalnum() and caracter != "-":
            return False
    return True


def validar_texto(texto):
    texto = texto.strip()
    if len(texto) == 0:
        return False

    for caracter in texto:
        if not caracter.isalnum() and caracter != " ":
            return False
    return True


def registrar_equipo():
    print("\n========== REGISTRAR EQUIPO ==========")

    codigo = input("Código del equipo: ")
    while not validar_codigo(codigo):
        print(" El código solo puede contener letras, números y guiones.")
        codigo = input("Código del equipo: ")

    equipos = cargar_datos(RUTA_EQUIPOS)

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            print(" Ese código ya está registrado.")
            return

    nombre = input("Nombre del equipo: ")
    while not validar_texto(nombre):
        print(" El nombre solo puede contener letras, números y espacios.")
        nombre = input("Nombre del equipo: ")
    tipo = input("Tipo de equipo: ")
    while not validar_texto(tipo):
        print(" El tipo solo puede contener letras, números y espacios.")
        tipo = input("Tipo de equipo: ")

    marca = input("Marca: ")
    while not validar_texto(marca):
        print(" La marca solo puede contener letras, números y espacios.")
        marca = input("Marca: ")

    nuevo_equipo = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "marca": marca,
        "estado": "Disponible"
    }

    equipos.append(nuevo_equipo)
    guardar_datos(RUTA_EQUIPOS, equipos)

    print("Equipo registrado correctamente.")




def mostrar_equipos():

    print("\n========== LISTA DE EQUIPOS ==========")

    equipos = cargar_datos(RUTA_EQUIPOS)

    if len(equipos) == 0:
        print("No hay equipos registrados.")
        return

    for equipo in equipos:
        print("----------------------------------")
        print(f"Código : {equipo['codigo']}")
        print(f"Nombre : {equipo['nombre']}")
        print(f"Tipo   : {equipo['tipo']}")
        print(f"Marca  : {equipo['marca']}")
        print(f"Estado : {equipo['estado']}")




def buscar_equipo():
    
    print("\n========== BUSCAR EQUIPO ==========")

    codigo = input("Código del equipo: ")

    equipos = cargar_datos(RUTA_EQUIPOS)

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            print("\nEquipo encontrado")
            print(f"Código : {equipo['codigo']}")
            print(f"Nombre : {equipo['nombre']}")
            print(f"Tipo   : {equipo['tipo']}")
            print(f"Marca  : {equipo['marca']}")
            print(f"Estado : {equipo['estado']}")
            return

    print("Equipo no encontrado.")
