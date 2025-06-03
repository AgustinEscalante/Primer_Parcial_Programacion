from Inputs import *
from Validaciones import *

def sumar_lista(lista: list) -> int:
    """Funcion para sumar los elementos de una lista

    Args:
        lista (list): Lista de numeros enteros

    Returns:
        int: Suma total de los elementos de la lista.
    """    
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total

def cargar_participantes(nombres: list):
    """  Carga los nombres de los participantes validando que cumplan con los requisitos:
    al menos 3 letras, y solo letras o espacios.

    Args:
        nombres (list): Lista donde se almacenarán los nombres de los 5 participantes.
    
    Returns:
        None
    """
    for i in range(5):
        while True:
            nombre = pedir_nombre(i)
            if validar_nombre(nombre):
                nombres[i] = nombre
                break
            else:
                print("Nombre inválido. Debe tener al menos 3 letras y solo contener letras o espacios.")

def cargar_puntajes(nombres: list, puntajes: list):
    """Carga los puntajes de cada jurado para cada participante. Valida que estén entre 1 y 10.

    Args:
        nombres (list): Lista con los nombres de los participantes.
        puntajes (list): Lista donde se almacenarán los puntajes de cada jurado para cada participante.
    
    Returns:
        None
    """
    for i in range(5):
        print(f"\nParticipante: {nombres[i]}")
        puntaje_jurado = [0, 0, 0]
        for j in range(3):
            puntaje = pedir_puntaje(j)
            while puntaje < 1 or puntaje > 10:
                print("Puntaje inválido. Debe ser entre 1 y 10.")
                puntaje = pedir_puntaje()
            puntaje_jurado[j] = puntaje
        puntajes[i] = puntaje_jurado

def mostrar_puntajes(nombres: list, puntajes: list) -> None:
    """Funcion que muestra los nombres de los participantes, sus puntajes individuales y el promedio.

    Args:
        nombres (list): Lista de nombres de los participantes.
        puntajes (list): Lista con los puntajes de cada participante.
    
    Returns:
        None
    """
    print("\n--- PUNTAJES ---")
    for i in range(5):
        promedio = sumar_lista(puntajes[i]) / 3
        print(f"Participante: {nombres[i]}")
        print(f"Jurado 1: {puntajes[i][0]}")
        print(f"Jurado 2: {puntajes[i][1]}")
        print(f"Jurado 3: {puntajes[i][2]}")
        print(f"Promedio: {promedio:.2f}\n")

def mostrar_promedios_mayores_a(nombres: list, puntajes: list, valor: int) -> None:
    """Fucnion que muestra los participantes cuyo promedio de puntajes es mayor al valor dado.

    Args:
        nombres (list): Lista de nombres de los participantes.
        puntajes (list): Lista con los puntajes de cada participante.
        valor (int): Valor límite a superar para mostrar el promedio.
    
    Returns:
        None
    """
    print(f"\n--- PROMEDIOS MAYORES A {valor} ---")
    bandera = False
    for i in range(5):
        promedio = sumar_lista(puntajes[i]) / 3
        if promedio > valor:
            print(f"{nombres[i]} - Promedio: {promedio:.2f}")
            bandera = True
    if not bandera:
        print(f"#ERROR - No hay participantes con promedio mayor a {valor}.")

def mostrar_promedios_jurados(puntajes: list):
    """Funcion que calcula y muestra el promedio de puntajes que dio cada jurado.

    Args:
        puntajes (list): Lista con los puntajes de todos los participantes.
    
    Returns:
        None
    """
    print("\n--- PROMEDIOS DE JURADOS ---")
    for j in range(3):
        suma = 0
        for i in range(5):
            suma += puntajes[i][j]
        promedio = suma / 5
        print(f"Jurado {j + 1}: {promedio:.2f}")

def mostrar_jurado_mas_estricto(puntajes: list):
    """Funcion para identificar y mostrar cuál fue el jurado más estricto, es decir, el que tuvo el promedio más bajo.

    Args:
        puntajes (list): Lista con los puntajes de todos los participantes.
    
    Returns:
        None
    """
    bandera = False
    menor_promedio = 0
    jurado_mas_estricto = 0

    for j in range(3):  
        suma = 0
        for i in range(5):  
            suma += puntajes[i][j]
        promedio = suma / 5

        if not bandera:
            menor_promedio = promedio
            jurado_mas_estricto = j + 1
            bandera = True
        elif promedio < menor_promedio:
            menor_promedio = promedio
            jurado_mas_estricto = j + 1
    print(f"\nEl jurado más estricto fue el Jurado {jurado_mas_estricto} con un promedio de {menor_promedio:.2f}")

def buscar_participante(nombres: list, puntajes: list):
    """Funcion que busca un participante por nombre (sin distinguir mayúsculas/minúsculas) y muestra sus puntajes y promedio.

    Args:
        nombres (list): Lista de nombres de los participantes.
        puntajes (list): Lista de listas con los puntajes por jurado para cada participante.
    
    Returns:
        None
    """    
    nombre_buscado = pedir_nombre_busqueda().lower()
    for i in range(5):
        if nombres[i].lower() == nombre_buscado:
            promedio = sumar_lista(puntajes[i]) / 3
            print(f"\nParticipante: {nombres[i]}")
            print(f"Jurado 1: {puntajes[i][0]}")
            print(f"Jurado 2: {puntajes[i][1]}")
            print(f"Jurado 3: {puntajes[i][2]}")
            print(f"Promedio: {promedio:.2f}")
            return
    print("Participante no encontrado.")
