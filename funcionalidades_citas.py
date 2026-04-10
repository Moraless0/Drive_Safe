import json, os
from utilidades import pedir_texto

def programar_cita():

    try:
        with open("data/clientes.json", "r") as f:
            clientes = json.load(f)
    except:
        clientes = []

    try:
        with open("data/instructores.json", "r") as f:
            instructores = json.load(f)
    except:
        instructores = []

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []
    
    try:
        with open("data/vehiculos.json", "r") as f:
            vehiculos = json.load(f)
    except:
        vehiculos = []

    # 🧾 CLIENTE
    doc_cliente = input("Documento del cliente: ")

    cliente = None
    for c in clientes:
        if str(c["documento"]) == doc_cliente:
            cliente = c
            break

    if cliente is None:
        print("❌ Cliente no existe")
        return

    print("✅ Cliente:", cliente["nombre"])

    # 🧾 INSTRUCTOR
    doc_instructor = input("Documento del instructor: ")

    instructor = None
    for i in instructores:
        if str(i["documento"]) == doc_instructor:
            instructor = i
            break

    if instructor is None:
        print("❌ Instructor no existe")
        pedir_texto("ENTER para continuar...")
        return

    print("✅ Instructor:", instructor["nombre"])

    # 🔥 VALIDAR TIPO
    if cliente["vehiculo"] != instructor["especialidad"]:
        print("❌ No coinciden (moto/carro)")
        pedir_texto("ENTER para continuar...")
        return

    # 🚗 BUSCAR VEHÍCULO DISPONIBLE
    vehiculo = None
    for v in vehiculos:
        if v["tipo"] == cliente["vehiculo"] and v.get("disponible", True):
            vehiculo = v
            break

    if vehiculo is None:
        print("❌ No hay vehículo disponible")
        pedir_texto("ENTER para continuar...")
        return

    print("✅ Vehículo:", vehiculo["placa"])

    # 📅 PEDIR DATOS
    fecha = input("Ingrese fecha (YYYY-MM-DD): ")
    hora = input("Ingrese hora (HH:MM): ")
    duracion = input("Ingrese duración (minutos): ")

    # 🔥 VALIDAR CONFLICTOS
    for cita in citas:
        if cita["fecha"] == fecha and cita["hora"] == hora:

            if cita["instructor"] == doc_instructor:
                print("❌ Instructor ocupado en ese horario")
                pedir_texto("ENTER para continuar...")
                return

            if cita["vehiculo"] == vehiculo["placa"]:
                print("❌ Vehículo ocupado en ese horario")
                pedir_texto("ENTER para continuar...")
                return

    # 🆕 CREAR CITA COMPLETA
    nueva_cita = {
        "id": len(citas) + 1,
        "cliente": doc_cliente,
        "instructor": doc_instructor,
        "vehiculo": vehiculo["placa"],
        "fecha": fecha,
        "hora": hora,
        "duracion": duracion,
        "asistencia": False,
        "observaciones": ""
    }

    citas.append(nueva_cita)

    # 🔥 CAMBIAR DISPONIBILIDAD VEHÍCULO
    for v in vehiculos:
        if v["placa"] == vehiculo["placa"]:
            v["disponible"] = False

    # 💾 GUARDAR TODO
    with open("data/citas.json", "w") as f:
        json.dump(citas, f, indent=4)

    with open("data/vehiculos.json", "w") as f:
        json.dump(vehiculos, f, indent=4)

    print("✅ Cita creada correctamente")
    pedir_texto("ENTER para continuar...")

def listar_citas():
    os.system("clear")
    try:
        with open("data/citas.json", "r") as archivo:
            citas = json.load(archivo)

        if not citas:
            print("No hay clientes registrados.")
        else:
            for cita in citas:
                print(f"ID: {cita['id']}")
                print(f"Cliente: {cita['cliente']}")
                print(f"Instructor: {cita['instructor']}")
                print(f"Vehículo: {cita['vehiculo']}")
                print(f"Fecha: {cita['fecha']}")
                print(f"Hora: {cita['hora']}")
                print(f"Duración: {cita['duracion']} min")
                print(f"Asistencia: {cita['asistencia']}")
                print(f"Observaciones: {cita['observaciones']}")
                print("=" * 40)

    except FileNotFoundError:
        print("El archivo clientes.json no existe.")

    except json.JSONDecodeError:
        print("El archivo está vacío o dañado.")

    except Exception as e:
        print("Error inesperado:", e)

    pedir_texto("Pulse ENTER para continuar...")