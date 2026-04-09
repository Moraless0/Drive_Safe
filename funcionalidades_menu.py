from utilidades_menu import mostrar_logo, pedir_opcion, pedir_opcion_clientes, pedir_opcion_instructores, pedir_opcion_vehiculos, pedir_opcion_citas, pedir_opcion_reporte
from funcionalidades_clientes import registrar_cliente, listar_clientes, buscar_cliente, eliminar_cliente
from funcionalidades_instructores import registrar_instructor, listar_instructores, eliminar_instructor
from funcionalidades_vehiculos import registrar_vehiculo, listar_vehiculos, cambiar_estado_vehiculo
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
                menu_gestionar_clientes()
            elif n == 2:
                os.system("clear")
                menu_gestionar_instructores()
            elif n == 3:
                os.system("clear")
                menu_gestionar_vehiculos()
            elif n == 4:
                os.system("clear")
                menu_gestionar_citas()
            elif n == 5:
                os.system("clear")
                menu_gestionar_reporte()
            elif n == 6:
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
            pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

def menu_gestionar_clientes():
    while True:
        try:
            os.system("clear")
            n = pedir_opcion_clientes()
            if n == 1:
                os.system("clear")
                registrar_cliente()
            elif n == 2:
                os.system("clear")
                listar_clientes()
            elif n == 3:
                os.system("clear")
                buscar_cliente()
            elif n == 4:
                os.system("clear")
                eliminar_cliente()
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
            pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

def menu_gestionar_instructores():
    while True:
        try:
            os.system("clear")
            n = pedir_opcion_instructores()
            if n == 1:
                os.system("clear")
                registrar_instructor()
            elif n == 2:
                os.system("clear")
                listar_instructores()
            elif n == 3:
                os.system("clear")
                eliminar_instructor()
            elif n == 4:
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

def menu_gestionar_vehiculos():
    while True:
        try:
            os.system("clear")
            n = pedir_opcion_vehiculos()
            if n == 1:
                os.system("clear")
                registrar_vehiculo()
            elif n == 2:
                os.system("clear")
                listar_vehiculos()
            elif n == 3:
                os.system("clear")
                cambiar_estado_vehiculo()
            elif n == 4:
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

def menu_gestionar_citas():
    while True:
        try:
            os.system("clear")
            n = pedir_opcion_citas()
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
                print("Opcion #5")
            elif n == 6:
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
            pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

def menu_gestionar_reporte():
    while True:
        try:
            os.system("clear")
            n = pedir_opcion_reporte()
            if n == 1:
                os.system("clear")
                print("Opción #1 - Agregar contacto nuevo")
            elif n == 2:
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