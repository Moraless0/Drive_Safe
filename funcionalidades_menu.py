from utilidades_menu import mostrar_logo, pedir_opcion, pedir_opcion_clientes, pedir_opcion_instructores, pedir_opcion_vehiculos, pedir_opcion_citas, pedir_opcion_reporte, pedir_opcion_evaluacion
from funcionalidades_clientes import registrar_cliente, listar_clientes, buscar_cliente, eliminar_cliente
from funcionalidades_instructores import registrar_instructor, listar_instructores, eliminar_instructor
from funcionalidades_vehiculos import registrar_vehiculo, listar_vehiculos, cambiar_estado_vehiculo
from funcionalidades_citas import programar_cita, listar_citas, listar_citas_cliente, listar_citas_fecha, registrar_asistencia
from funcionalidades_reporte import reporte_cliente, reporte_fecha, resumen_general, citas_por_instructor, uso_vehiculos, inasistencias
from funcionalidades_evaluaciones import registrar_evaluacion, listar_calificaciones_estudiante, promedio_calificaciones
from utilidades import pedir_texto, limpiar_pantalla

def seleccionar_opción():
    while True:
        try:
            limpiar_pantalla()
            mostrar_logo()
            n = pedir_opcion()
            if n == 1:
                limpiar_pantalla()
                menu_gestionar_clientes()
            elif n == 2:
                limpiar_pantalla()
                menu_gestionar_instructores()
            elif n == 3:
                limpiar_pantalla()
                menu_gestionar_vehiculos()
            elif n == 4:
                limpiar_pantalla()
                menu_gestionar_citas()
            elif n == 5:
                limpiar_pantalla()
                menu_gestionar_reporte()
            elif n == 6:
                limpiar_pantalla()
                menu_gestionar_evaluaciones()
            elif n == 7:
                limpiar_pantalla()
                print("Saliendo del programa...")
                break
            else:
                limpiar_pantalla()
                print("Opcion no valida!")
                print("Ingrese un valor correcto!")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("data/error.txt", "a") as archivo:
                 archivo.write(f"ERROR: Opción inválida = {n}\n\n")

                    
        except Exception:
            limpiar_pantalla()
            print("ERROR - INCORRECTO")
            pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

def menu_gestionar_clientes():
    while True:
        try:
            limpiar_pantalla()
            n = pedir_opcion_clientes()
            if n == 1:
                limpiar_pantalla()
                registrar_cliente()
            elif n == 2:
                limpiar_pantalla()
                listar_clientes()
            elif n == 3:
                limpiar_pantalla()
                buscar_cliente()
            elif n == 4:
                limpiar_pantalla()
                eliminar_cliente()
            elif n == 5:
                limpiar_pantalla()
                print("Saliendo del programa...")
                break
            else:
                limpiar_pantalla()
                print("Opcion no valida!")
                print("Ingrese un valor correcto!")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("data/error.txt", "a") as archivo:
                    archivo.write(f"ERROR: Opción inválida = {n}\n\n")
        
        except Exception:
            limpiar_pantalla()
            print("ERROR - INCORRECTO")
            pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

def menu_gestionar_instructores():
    while True:
        try:
            limpiar_pantalla()
            n = pedir_opcion_instructores()
            if n == 1:
                limpiar_pantalla()
                registrar_instructor()
            elif n == 2:
                limpiar_pantalla()
                listar_instructores()
            elif n == 3:
                limpiar_pantalla()
                eliminar_instructor()
            elif n == 4:
                limpiar_pantalla()
                print("Saliendo del programa...")
                break
            else:
                limpiar_pantalla()
                print("Opcion no valida!")
                print("Ingrese un valor correcto!")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("data/error.txt", "a") as archivo:
                    archivo.write(f"ERROR: Opción inválida = {n}\n\n")
        
        except Exception:
            limpiar_pantalla()
            print("ERROR - INCORRECTO")

def menu_gestionar_vehiculos():
    while True:
        try:
            limpiar_pantalla()
            n = pedir_opcion_vehiculos()
            if n == 1:
                limpiar_pantalla()
                registrar_vehiculo()
            elif n == 2:
                limpiar_pantalla()
                listar_vehiculos()
            elif n == 3:
                limpiar_pantalla()
                cambiar_estado_vehiculo()
            elif n == 4:
                limpiar_pantalla()
                print("Saliendo del programa...")
                break
            else:
                limpiar_pantalla()
                print("Opcion no valida!")
                print("Ingrese un valor correcto!")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("data/error.txt", "a") as archivo:
                 archivo.write(f"ERROR: Opción inválida = {n}\n\n")
        
        except Exception:
            limpiar_pantalla()
            print("ERROR - INCORRECTO")

def menu_gestionar_citas():
    while True:
        try:
            limpiar_pantalla()
            n = pedir_opcion_citas()
            if n == 1:
                limpiar_pantalla()
                programar_cita()
            elif n == 2:
                limpiar_pantalla()
                listar_citas()
            elif n == 3:
                limpiar_pantalla()
                listar_citas_cliente()
            elif n == 4:
                limpiar_pantalla()
                listar_citas_fecha()
            elif n == 5:
                registrar_asistencia()
            elif n == 6:
                limpiar_pantalla()
                print("Saliendo del programa...")
                break
            else:
                limpiar_pantalla()
                print("Opcion no valida!")
                print("Ingrese un valor correcto!")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("data/error.txt", "a") as archivo:
                 archivo.write(f"ERROR: Opción inválida = {n}\n\n")

                    
        except Exception:
            limpiar_pantalla()
            print("ERROR - INCORRECTO")
            pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

def menu_gestionar_reporte():
    while True:
        try:
            limpiar_pantalla()
            n = pedir_opcion_reporte()
            if n == 1:
                limpiar_pantalla()
                reporte_cliente()
            elif n == 2:
                limpiar_pantalla()
                reporte_fecha()
            elif n == 3:
                limpiar_pantalla()
                resumen_general()
            elif n == 4:
                limpiar_pantalla()
                citas_por_instructor()
            elif n == 5:
                limpiar_pantalla()
                uso_vehiculos()
            elif n == 6:
                limpiar_pantalla()
                inasistencias()
            elif n == 7:
                limpiar_pantalla()
                print("Saliendo del programa...")
                break
            else:
                limpiar_pantalla()
                print("Opcion no valida!")
                print("Ingrese un valor correcto!")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("data/error.txt", "a") as archivo:
                 archivo.write(f"ERROR: Opción inválida = {n}\n\n")
        
        except Exception:
            print("ERROR - INCORRECTO")
            pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)
            
def menu_gestionar_evaluaciones():
    while True:
        try:
            limpiar_pantalla()
            n = pedir_opcion_evaluacion()
            if n == 1:
                limpiar_pantalla()
                registrar_evaluacion()
            elif n == 2:
                limpiar_pantalla()
                listar_calificaciones_estudiante()
            elif n == 3:
                limpiar_pantalla()
                promedio_calificaciones()
            elif n == 4:
                limpiar_pantalla()
                print("Saliendo del programa...")
                break
            else:
                limpiar_pantalla()
                print("Opcion no valida!")
                print("Ingrese un valor correcto!")
                pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)

                with open("data/error.txt", "a") as archivo:
                 archivo.write(f"ERROR: Opción inválida = {n}\n\n")
        
        except Exception:
            print("ERROR - INCORRECTO")
            pedir_texto("Pulse ENTER para intentar nuevamente.", permitir_vacio=True)