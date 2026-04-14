from utilidades import pedir_texto, limpiar_pantalla
import json

import json

def registrar_vehiculo():
    placa = input("Ingrese la placa del vehículo: ").strip().upper()

    while True:
        tipo = input("Ingrese tipo de vehículo (moto/carro): ").strip().capitalize()
        if tipo in ["Moto", "Carro"]:
            break
        else:
            print("❌ Solo se permite 'Moto' o 'Carro'")

    marca = input("Ingrese la marca del vehículo: ").strip().capitalize()
    modelo = input("Ingrese el modelo del vehículo: ").strip().capitalize()
    anio = input("Ingrese el año del vehículo: ").strip()

    disponible = True

    vehiculo = {
        "placa": placa,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "anio": anio,
        "disponible": disponible
    }

    try:
        with open("data/vehiculos.json", "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    for v in datos:
        if v["placa"] == placa:
            print("❌ Ya existe un vehículo con esa placa")
            pedir_texto("ENTER para continuar", permitir_vacio=True)
            return

    datos.append(vehiculo)

    with open("data/vehiculos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print("✅ Vehículo registrado correctamente")
    pedir_texto("ENTER para continuar", permitir_vacio=True)

def listar_vehiculos():
    limpiar_pantalla()
    try:
        with open("data/vehiculos.json", "r") as archivo:
            vehiculos = json.load(archivo)

        if not vehiculos:
            print("No hay vehiculos registrados.")
        else:
            for vehiculo in vehiculos:

                estado = "DISPONIBLE ✅" if vehiculo.get("disponible") else "NO DISPONIBLE ❌"

                print("Marca: ", vehiculo.get("marca", ""))
                print("Modelo: ", vehiculo.get("modelo", ""))
                print("Tipo:", vehiculo.get("tipo", ""))
                print("Año:", vehiculo.get("anio", ""))
                print("Placa:", vehiculo.get("placa", ""))
                print("Disponible: ", estado)
                print("==" * 18)

    except FileNotFoundError:
        print("El archivo vehiculos.json no existe.")

    except json.JSONDecodeError:
        print("El archivo está vacío o dañado.")

    except Exception as e:
        print("Error inesperado:", e)

    pedir_texto("ENTER para continuar", permitir_vacio=True)

def cambiar_estado_vehiculo():
    limpiar_pantalla()

    placa = input("Ingrese la placa del vehículo: ").strip().upper()

    try:
        with open("data/vehiculos.json", "r") as archivo:
            vehiculos = json.load(archivo)
    except:
        print("❌ Error al leer el archivo")
        input("ENTER para continuar...")
        return

    encontrado = False

    for v in vehiculos:
        if v["placa"] == placa:
            v["disponible"] = not v["disponible"]

            estado = "DISPONIBLE ✅" if v["disponible"] else "NO DISPONIBLE ❌"
            print(f"🚗 El vehículo con placa {placa} ahora está {estado}")

            encontrado = True
            break

    if not encontrado:
        print("❌ Vehículo no encontrado")

    with open("data/vehiculos.json", "w") as archivo:
        json.dump(vehiculos, archivo, indent=4)

    pedir_texto("ENTER para continuar", permitir_vacio=True)