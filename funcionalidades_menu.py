from utilidades_menu import mostrar_logo, pedir_opcion
from utilidades import pedir_texto
import os

def seleccionar_opción():
    while True:
        try:
            os.system("clear")
            mostrar_logo()
            n = pedir_opcion()
            if n == 1:
                os.system("clear")
                print("Opción #1 - Agregar contacto nuevo")
            elif n == 2:
                os.system("clear")
                print("Opción #2 - Eliminar contacto")
            elif n == 3:
                os.system("clear")
                print("Opción #3 - Buscar contacto")
            elif n == 4:
                os.system("clear")
                print("Opción #4 - Mostrar todos los contactos")
            elif n == 5:
                os.system("clear")
                print("Saliendo del programa...")
                break
            else:
                os.system("clear")
                print("Opcion no valida!")
                print("Ingrese un valor correcto!")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("error.txt", "a") as archivo:
                 archivo.write(f"ERROR: Opción inválida = {n}\n\n")

                    
        except Exception:
            os.system("clear")
            print("ERROR - INCORRECTO")