import os

def pedir_texto(mensaje, permitir_vacio=False):
    try:
        opc = input(mensaje).strip()
        
        if not permitir_vacio and opc == "":
            print("Se debe ingresar un valor!")
            return None
        
        return opc

    except Exception:
        print("Error al pedir texto!")
        return None

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')