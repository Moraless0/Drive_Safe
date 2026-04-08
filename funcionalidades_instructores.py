from utilidades import pedir_texto
import json, os

def registrar_instructor():
    nombre = input("Ingrese el nombre del instructor ").capitalize()
    nombre = input("Ingrese el apellido del instructor ").capitalize()
    documento = int(input("Ingrese el documento del instructor "))
    especialidad = input("Ingrese el tipo de vehiculo a instruir ").capitalize()

    instructores = {
        "nombre" : nombre, "documento" : documento, "vehiculo" : tipo_de_vehiculo
        }

    try:
        with open("clientes.json", "r") as archivo:
            datos = json.load(archivo)
    
    except:
        datos = []
        
    datos.append(instructores)

    with open("clientes.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def listar_clientes():
    os.system("clear")
    try:
        with open("clientes.json", "r") as archivo:
            clientes = json.load(archivo)

        if not clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in clientes:
                print("Nombre:", cliente.get("nombre", ""), cliente.get("apellido", ""))
                print("Documento:", cliente.get("documento", ""))
                print("Tipo de vehículo:", cliente.get("tipo_vehiculo", ""))
                print("==" * 18)

    except FileNotFoundError:
        print("El archivo clientes.json no existe.")

    except json.JSONDecodeError:
        print("El archivo está vacío o dañado.")

    except Exception as e:
        print("Error inesperado:", e)

    pedir_texto("Pulse ENTER para continuar...")

def buscar_cliente():
    nombre_buscar = input("Ingrese el nombre del cliente: ").strip().lower()

    try:
        with open("clientes.json", "r") as archivo:
            clientes = json.load(archivo)
        
        encontrado = False

        for cliente in clientes:
            if cliente.get("nombre", "").lower() == nombre_buscar:

                print(f"""
Nombre: {cliente.get('nombre', '')} {cliente.get('apellido', '')}
Documento: {cliente.get('documento', '')}
Tipo de vehículo: {cliente.get('vehiculo', '')}
{"=="*15}
""")
                encontrado = True

        if not encontrado:
            print("No se encontró el cliente")
            with open("error.txt", "a") as archivo:
                archivo.write("Usuario intentó buscar cliente inexistente\n")

    except FileNotFoundError:
        print("El archivo clientes.json no existe")

    except json.JSONDecodeError:
        print("El archivo está vacío o dañado")

    except Exception as e:
        print("Error:", e)

    pedir_texto("Pulse ENTER para continuar...")