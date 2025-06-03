from Validaciones import *

def pedir_nombre(i: int) -> str:
    """Pide y valida el nombre de un participante

    Args:
        i (int): _description_

    Returns:
        str: _description_
    """    
    while True:
        nombre = input(f"Ingrese el nombre del participante {i+1}: ")
        if validar_nombre(nombre):
            return nombre
        else:
            print("Nombre inválido. Debe tener al menos 3 letras y solo letras o espacios.")

def pedir_puntaje(jurado: int) -> int:
    """Solicita al usuario un puntaje válido (entero entre 1 y 10). Repite si hay errores.

    Args:
        jurado (int):Ingresa un entero entre 1 y 10

    Returns:
        int: Devuelve un entero entre 1 y 10
    """    
    while True:
        entrada = input(f"Ingrese puntaje del Jurado {jurado+1} (1-10): ")
        bandera = True
        for i in entrada:
            if ord(i) < 48 or ord(i) > 57:
                bandera = False
                break
        if bandera:
            puntaje = int(entrada)
            if 1 <= puntaje <= 10:
                return puntaje
            else:
                print("Puntaje fuera de rango. Debe estar entre 1 y 10.")
        else:
            print("Entrada inválida. Ingrese solo números del 1 al 10.")

def pedir_nombre_busqueda() -> str:
    return input("Ingrese el nombre del participante a buscar: ")
