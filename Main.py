from Menu import *

nombres = ["" for i in range(5)]
puntajes = [[] for i in range(5)]

while True:
    mostrar_menu()
    opcion = ingresar_opcion()
    manejar_menu(opcion, nombres, puntajes)
