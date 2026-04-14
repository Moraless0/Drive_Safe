from utilidades import pedir_texto, limpiar_pantalla
import json

def reporte_cliente():

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

def reporte_fecha():

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

def resumen_general():

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

    if not citas:
        print("❌ No hay datos")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    total = len(citas)
    asistieron = sum(1 for c in citas if c["asistencia"] == True)
    no_asistieron = sum(1 for c in citas if c["asistencia"] == False)
    pendientes = sum(1 for c in citas if c["asistencia"] == False and c["observaciones"] == "")

    print(f"""
=== 📊 RESUMEN GENERAL ===
Total citas: {total}
Asistieron: {asistieron} ✅
No asistieron: {no_asistieron} ❌
Pendientes: {pendientes} ⏳
""")

    pedir_texto("ENTER para continuar...", permitir_vacio=True)

def citas_por_instructor():

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

    if not citas:
        print("❌ No hay citas")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    conteo = {}

    for c in citas:
        instructor = c["instructor"]
        conteo[instructor] = conteo.get(instructor, 0) + 1

    print("\n📊 CITAS POR INSTRUCTOR:\n")

    for instructor, cantidad in conteo.items():
        print(f"Instructor {instructor}: {cantidad} citas")

    pedir_texto("ENTER para continuar...", permitir_vacio=True)

def uso_vehiculos():

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

    if not citas:
        print("❌ No hay datos")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    conteo = {}

    for c in citas:
        vehiculo = c["vehiculo"]
        conteo[vehiculo] = conteo.get(vehiculo, 0) + 1

    print("\n🚗 USO DE VEHÍCULOS:\n")

    for vehiculo, cantidad in conteo.items():
        print(f"{vehiculo}: {cantidad} usos")

    pedir_texto("ENTER para continuar...", permitir_vacio=True)

def inasistencias():

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

    if not citas:
        print("❌ No hay citas")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    print("\n❌ CITAS CON INASISTENCIA:\n")

    encontrado = False

    for c in citas:
        if c["asistencia"] == False:
            encontrado = True
            print(f"""
🆔 ID: {c['id']}
👤 Cliente: {c['cliente']}
📅 Fecha: {c['fecha']}
⏰ Hora: {c['hora']}
🚗 Vehículo: {c['vehiculo']}
📝 Observaciones: {c['observaciones']}
""")
            print("=="*15)

    if not encontrado:
        print("✅ No hay inasistencias registradas")

    pedir_texto("ENTER para continuar...", permitir_vacio=True)