
from estudiantes import registrar_estudiante, mostrar_estudiantes, buscar_estudiante
from equipos import registrar_equipo, mostrar_equipos, buscar_equipo
from prestamos import prestar_equipo, devolver_equipo, mostrar_historial


def menu():

    while True:

        print("\n")
        print("==========================================")
        print("   SISTEMA DE PRÉSTAMO DE EQUIPOS")
        print("==========================================")
        print("1. Registrar estudiante")
        print("2. Registrar equipo")
        print("3. Mostrar estudiantes")
        print("4. Mostrar equipos")
        print("5. Buscar estudiante")
        print("6. Buscar equipo")
        print("7. Prestar equipo")
        print("8. Devolver equipo")
        print("9. Historial de préstamos")
        print("10. Salir")
        print("==========================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()

        elif opcion == "2":
            registrar_equipo()

        elif opcion == "3":
            mostrar_estudiantes()

        elif opcion == "4":
            mostrar_equipos()

        elif opcion == "5":
            buscar_estudiante()

        elif opcion == "6":
            buscar_equipo()

        elif opcion == "7":
            prestar_equipo()

        elif opcion == "8":
            devolver_equipo()

        elif opcion == "9":
            mostrar_historial()

        elif opcion == "10":
            print("\nSistema cerrado.")
            break

        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    menu()