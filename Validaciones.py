def validar_nombre(nombre: str) -> bool:

    """ Funcion que valida si un nombre es válido.
    Un nombre es válido si tiene al menos 3 letras y solo contiene letras (mayúsculas o minúsculas) y espacios.

    Args:
        nombre (str): descripción del nombre a validar_.

    Returns:
        bool: Devuelve True si el nombre es válido, False en caso contrario.
    """    
    if len(nombre) < 3:
        return False
    for i in nombre:
        ascii_code = ord(i)
        if not ((65 <= ascii_code <= 90) or (97 <= ascii_code <= 122) or ascii_code == 32):
            return False
    return True

def verificar_puntajes_cargados(puntajes: list) -> bool:
    resultado = True
    if puntajes[0] == []:
        print("\nPrimero debe cargar las puntuaciones (opción 2).")
        resultado = False
    return resultado