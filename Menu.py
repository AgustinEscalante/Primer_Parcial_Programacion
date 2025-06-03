from Funciones import *
from Validaciones import *

def mostrar_menu() -> None:
    """Funcion para desplegar un menu"""    

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Cargar participantes")
    print("2. Cargar puntuaciones")
    print("3. Mostrar puntuaciones")
    print("4. Promedios > 4")
    print("5. Promedios > 7")
    print("6. Promedio de cada jurado")
    print("7. Jurado más estricto")
    print("8. Buscar participante")
    print("9. Salir")

def ingresar_opcion():
    """Funcion para ingresar opcion en el menu con validacion """    
    
    while True:
        opcion = input("Elija una opción (1-9): ")

        if opcion == "":
            print("No ingresó ninguna opción, intente de nuevo.\n")
            continue

        bandera = True
        for i in opcion:
            if ord(i) < 48 or ord(i) > 57:
                bandera = False
                break

        if bandera:
            numero = int(opcion)
            if 1 <= numero <= 9:
                return numero
            else:
                print("Numero incorrecto. Ingrese un número entre 1 y 9.")
        else:
            print("Incorrecto, solo se permite un número  entre 1 y 9.")

def manejar_menu(opcion: int, nombres: list, puntajes: list) -> None:
    """Funcion para ejecutar la acción correspondiente según la opción seleccionada del menú.

    Args:
        opcion (int): Número de opción seleccionada por el usuario (1 a 9).
        nombres (list): Lista con los nombres de los participantes.
        puntajes (list): Lista de listas con las puntuaciones por jurado de cada participante.

    """    
    if opcion == 1:
        cargar_participantes(nombres)
        
    elif opcion == 2:
        if nombres[0] == "":
            print("\nPrimero debe cargar los participantes (opción 1).")
        else:
            cargar_puntajes(nombres, puntajes)

    elif opcion == 3:
        if verificar_puntajes_cargados(puntajes):
            mostrar_puntajes(nombres, puntajes)

    elif opcion == 4:
        if verificar_puntajes_cargados(puntajes):
            mostrar_promedios_mayores_a(nombres, puntajes, 4)

    elif opcion == 5:
        if verificar_puntajes_cargados(puntajes):
            mostrar_promedios_mayores_a(nombres, puntajes, 7)

    elif opcion == 6:
        if verificar_puntajes_cargados(puntajes):
            mostrar_promedios_jurados(puntajes)

    elif opcion == 7:
        if verificar_puntajes_cargados(puntajes):
            mostrar_jurado_mas_estricto(puntajes)

    elif opcion == 8:
        if verificar_puntajes_cargados(puntajes):
            buscar_participante(nombres, puntajes)

    elif opcion == 9:
        print("Saliendo del programa...")
        exit()

    else:
        print("Opción inválida.")

    input("\nPresione Enter para continuar...")
