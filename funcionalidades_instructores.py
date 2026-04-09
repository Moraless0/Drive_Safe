from utilidades import pedir_texto
import json, os

def registrar_instructor():
    nombre = input("Ingrese el nombre del instructor ").capitalize()
    apellido = input("Ingrese el apellido del instructor ").capitalize()
    documento = int(input("Ingrese el documento del instructor "))
    
    while True:
        tipo = input("Ingrese tipo de vehículo (moto/carro): ").strip().capitalize()
        if tipo in ["Moto", "Carro"]:
            break
        else:
            print("❌ Solo se permite 'Moto' o 'Carro'")

    try:
        with open("instructores.json", "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    for i in datos:
        if i["documento"] == documento:
            print("❌ Ya existe un instructor con ese documento")
            pedir_texto("ENTER para continuar...")
            return

    ids = [i["id"] for i in datos if "id" in i]
    nuevo_id = max(ids) + 1 if ids else 1

    instructores = {
        "id": nuevo_id,
        "nombre" : nombre,
        "apellido" : apellido,
        "documento" : documento,
        "especialidad" : tipo
    }

    datos.append(instructores)

    with open("instructores.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
    
    print("✅ Instructor registrado correctamente")
    pedir_texto("ENTER para continuar...")

def listar_instructores():
    os.system("clear")
    try:
        with open("instructores.json", "r") as archivo:
            instructores = json.load(archivo)

        if not instructores:
            print("No hay instructores registrados.")
        else:
            for instructor in instructores:
                print("ID:", instructor.get("id", ""))
                print("Nombre:", instructor.get("nombre", ""), instructor.get("apellido", ""))
                print("Documento:", instructor.get("documento", ""))
                print("Tipo de vehículo:", instructor.get("especialidad", ""))
                print("==" * 18)

    except FileNotFoundError:
        print("El archivo instructores.json no existe.")

    except json.JSONDecodeError:
        print("El archivo está vacío o dañado.")

    except Exception as e:
        print("Error inesperado:", e)

    pedir_texto("Pulse ENTER para continuar...")

def eliminar_instructor():
    nombre = input("Ingrese el nombre del instructor a eliminar: ").capitalize()

    with open("instructores.json", "r") as archivo:
        instructor = json.load(archivo)
        
        nueva_lista = [c for c in instructor if c["nombre"]!= nombre]
        
        if len (instructor) == len(nueva_lista):
            print("No se encontró el instructor")
            with open("error.txt", "a") as archivo:
                archivo.write("Usuario intenta eliminar instructor no existente\n\n")
                pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)
        else:
            print("Instructor eliminado correctamente")
            pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)
                
        with open("instructores.json", "w") as archivo:
            json.dump(nueva_lista, archivo, indent=4)

    
