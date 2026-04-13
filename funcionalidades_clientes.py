from utilidades import pedir_texto, limpiar_pantalla
import json, os

def registrar_cliente():
    nombre = input("Ingrese el nombre del cliente ").capitalize()
    apellido = input("Ingrese el apellido del cliente ").capitalize()
    documento = input("Ingrese el documento del cliente ")
    
    while True:
        tipo = input("Ingrese tipo de vehículo (moto/carro): ").strip().capitalize()
        if tipo in ["Moto", "Carro"]:
            break
        else:
            print("❌ Solo se permite 'Moto' o 'Carro'")

    clientes = {
        "documento" : documento,"nombre" : nombre, "apellido" : apellido,  "vehiculo" : tipo
        }

    try:
        with open("data/clientes.json", "r") as archivo:
            datos = json.load(archivo)
    
    except:
        datos = []
        
    datos.append(clientes)

    with open("data/clientes.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
    
    print("✅ Cliente registrado correctamente")
    pedir_texto("ENTER para continuar", permitir_vacio=True)

def listar_clientes():
    limpiar_pantalla()
    try:
        with open("data/clientes.json", "r") as archivo:
            clientes = json.load(archivo)

        if not clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in clientes:
                print("Nombre:", cliente.get("nombre", ""), cliente.get("apellido", ""))
                print("Documento:", cliente.get("documento", ""))
                print("Tipo de vehículo:", cliente.get("vehiculo", ""))
                print("==" * 18)

    except FileNotFoundError:
        print("El archivo clientes.json no existe.")

    except json.JSONDecodeError:
        print("El archivo está vacío o dañado.")

    except Exception as e:
        print("Error inesperado:", e)

    pedir_texto("ENTER para continuar", permitir_vacio=True)

def buscar_cliente():
    nombre_buscar = input("Ingrese el nombre del cliente: ").strip().lower()

    try:
        with open("data/clientes.json", "r") as archivo:
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
            with open("data/error.txt", "a") as archivo:
                archivo.write("Usuario intentó buscar cliente inexistente\n")

    except FileNotFoundError:
        print("El archivo clientes.json no existe")

    except json.JSONDecodeError:
        print("El archivo está vacío o dañado")

    except Exception as e:
        print("Error:", e)

    pedir_texto("ENTER para continuar", permitir_vacio=True)

def eliminar_cliente():
    nombre = input("Ingrese el nombre del cliente a eliminar: ").capitalize()

    with open("data/clientes.json", "r") as archivo:
        cliente = json.load(archivo)
        
        nueva_lista = [c for c in cliente if c["nombre"]!= nombre]
        
        if len (cliente) == len(nueva_lista):
            print("No se encontró el cliente")
            with open("data/error.txt", "a") as archivo:
                archivo.write("Usuario intenta eliminar cliente no existente\n\n")
                pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)
        else:
            print("Cliente eliminado correctamente")
            pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)
                
        with open("data/clientes.json", "w") as archivo:
            json.dump(nueva_lista, archivo, indent=4)