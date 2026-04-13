import json, os
from utilidades import pedir_texto, limpiar_pantalla

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

    doc_cliente = input("Documento del cliente: ")

    cliente = None
    for c in clientes:
        if str(c["documento"]) == doc_cliente:
            cliente = c
            break

    if cliente is None:
        print("❌ Cliente no existe")
        pedir_texto("ENTER para continuar", permitir_vacio=True)
        return

    print("✅ Cliente:", cliente["nombre"])

    doc_instructor = input("Documento del instructor: ")

    instructor = None
    for i in instructores:
        if str(i["documento"]) == doc_instructor:
            instructor = i
            

    if instructor is None:
        print("❌ Instructor no existe")
        pedir_texto("ENTER para continuar", permitir_vacio=True)
        return

    print("✅ Instructor:", instructor["nombre"])

    if cliente["vehiculo"] != instructor["especialidad"]:
        print("❌ No coinciden (moto/carro)")
        pedir_texto("ENTER para continuar", permitir_vacio=True)
        return

    vehiculo = None
    for v in vehiculos:
        if v["tipo"] == cliente["vehiculo"] and v.get("disponible", True):
            vehiculo = v
            break

    if vehiculo is None:
        print("❌ No hay vehículo disponible")
        pedir_texto("ENTER para continuar", permitir_vacio=True)
        return

    print("✅ Vehículo:", vehiculo["placa"])

    fecha = input("Ingrese fecha (YYYY-MM-DD): ")
    hora = input("Ingrese hora (HH:MM): ")
    duracion = input("Ingrese duración (minutos): ")

    for cita in citas:
        if cita["fecha"] == fecha and cita["hora"] == hora:

            if cita["instructor"] == doc_instructor:
                print("❌ Instructor ocupado en ese horario")
                pedir_texto("ENTER para continuar", permitir_vacio=True)
                return

            if cita["vehiculo"] == vehiculo["placa"]:
                print("❌ Vehículo ocupado en ese horario")
                pedir_texto("ENTER para continuar", permitir_vacio=True)
                return

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

    for v in vehiculos:
        if v["placa"] == vehiculo["placa"]:
            v["disponible"] = False

    with open("data/citas.json", "w") as f:
        json.dump(citas, f, indent=4)

    with open("data/vehiculos.json", "w") as f:
        json.dump(vehiculos, f, indent=4)

    print("✅ Cita creada correctamente")
    pedir_texto("ENTER para continuar", permitir_vacio=True)

def listar_citas():

    limpiar_pantalla()

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

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

    if not citas:
        print("❌ No hay citas registradas")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    print("\n📋 LISTADO DE CITAS:\n")

    for c in citas:

        nombre_cliente = "Desconocido"
        for cl in clientes:
            if str(cl["documento"]) == str(c["cliente"]):
                nombre_cliente = cl["nombre"]
                break

        nombre_instructor = "Desconocido"
        for i in instructores:
            if str(i["documento"]) == str(c["instructor"]):
                nombre_instructor = i["nombre"]
                break

        print(f"""
🆔 ID: {c['id']}
👤 Cliente: {nombre_cliente}
👨‍🏫 Instructor: {nombre_instructor}
🚗 Vehículo: {c['vehiculo']}
📅 Fecha: {c['fecha']}
⏰ Hora: {c['hora']}
⌛ Duración: {c['duracion']} min
✅ Asistencia: {"Sí" if c['asistencia'] else "No"}
📝 Observaciones: {c['observaciones']}
""")
        print("=="*20)

    pedir_texto("Pulse ENTER para continuar...", permitir_vacio=True)

def listar_citas_cliente():

    doc_cliente = input("Ingrese el documento del cliente: ")

    try:
        with open("data/clientes.json", "r") as f:
            clientes = json.load(f)
    except:
        clientes = []

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

    cliente = None
    for c in clientes:
        if str(c["documento"]) == doc_cliente:
            cliente = c
            break

    if cliente is None:
        print("❌ Cliente no existe")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    print(f"\n📋 Citas de {cliente['nombre']}:\n")

    encontrado = False

    for c in citas:
        if str(c["cliente"]) == doc_cliente:
            encontrado = True
            print(f"""
🆔 ID: {c['id']}
📅 Fecha: {c['fecha']}
⏰ Hora: {c['hora']}
🚗 Vehículo: {c['vehiculo']}
👨‍🏫 Instructor: {c['instructor']}
⌛ Duración: {c['duracion']} min
✅ Asistencia: {"Sí" if c['asistencia'] else "No"}
📝 Observaciones: {c['observaciones']}
""")
            print("=="*15)

    if not encontrado:
        print("❌ Este cliente no tiene citas")
    
    pedir_texto("ENTER para continuar...", permitir_vacio=True)

def listar_citas_fecha():

    fecha_buscar = input("Ingrese la fecha (YYYY-MM-DD): ")

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

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

    print(f"\n📅 Citas para la fecha {fecha_buscar}:\n")

    encontrado = False

    for c in citas:
        if c["fecha"] == fecha_buscar:
            encontrado = True

            nombre_cliente = "Desconocido"
            for cl in clientes:
                if str(cl["documento"]) == str(c["cliente"]):
                    nombre_cliente = cl["nombre"]
                    break

            nombre_instructor = "Desconocido"
            for i in instructores:
                if str(i["documento"]) == str(c["instructor"]):
                    nombre_instructor = i["nombre"]
                    break

            print(f"""
🆔 ID: {c['id']}
👤 Cliente: {nombre_cliente}
👨‍🏫 Instructor: {nombre_instructor}
🚗 Vehículo: {c['vehiculo']}
⏰ Hora: {c['hora']}
⌛ Duración: {c['duracion']} min
✅ Asistencia: {"Sí" if c['asistencia'] else "No"}
📝 Observaciones: {c['observaciones']}
""")
            print("=="*15)

    if not encontrado:
        print("❌ No hay citas para esta fecha")

    pedir_texto("ENTER para continuar...", permitir_vacio=True)

def registrar_asistencia():

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

    if not citas:
        print("❌ No hay citas registradas")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    id_cita = input("Ingrese el ID de la cita: ")

    cita_encontrada = None

    for c in citas:
        if str(c["id"]) == id_cita:
            cita_encontrada = c
            break

    if cita_encontrada is None:
        print("❌ Cita no encontrada")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    print(f"""
📅 Fecha: {cita_encontrada['fecha']}
⏰ Hora: {cita_encontrada['hora']}
👤 Cliente: {cita_encontrada['cliente']}
👨‍🏫 Instructor: {cita_encontrada['instructor']}
""")

    while True:
        asistencia = input("¿Asistió? (s/n): ").strip().lower()
        if asistencia in ["s", "n"]:
            cita_encontrada["asistencia"] = True if asistencia == "s" else False
            break
        else:
            print("❌ Opción inválida")

    observacion = input("Ingrese observación: ").strip()
    cita_encontrada["observaciones"] = observacion

    with open("data/citas.json", "w") as f:
        json.dump(citas, f, indent=4)

    print("✅ Asistencia y observación registradas correctamente")
    pedir_texto("ENTER para continuar...", permitir_vacio=True)