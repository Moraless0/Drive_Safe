from utilidades import pedir_texto
from datetime import datetime
import json

def registrar_evaluacion():
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
        with open("data/evaluaciones.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

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
        print("❌ Instructor no se especializa en el tipo de vehículo del cliente")
        pedir_texto("ENTER para continuar", permitir_vacio=True)
        return

    fecha = input("Ingrese fecha (YYYY-MM-DD): ")

# Validar fecha y hora
    try:
        fecha_cita = datetime.strptime(f"{fecha}", "%Y-%m-%d")
    except ValueError:
        print("❌ Fecha u hora inválida")
        pedir_texto("ENTER para continuar...")
        return

# Validar que no sea en el futuro
    if fecha_cita > datetime.now():
        print("❌ No puedes crear una cita en el futuro, solo fechas actuales o pasadas")
        pedir_texto("ENTER para continuar", permitir_vacio=True)
        return
    
    pts_cliente = input("Calificación del cliente (0-100): ")
    
    if pts_cliente == "":
        print("❌ Calificación no puede estar vacía")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return
    else:
        try:
            pts_cliente = int(pts_cliente)
            if pts_cliente < 0 or pts_cliente > 100:
                print("❌ Calificación debe ser entre 0 y 100")
                pedir_texto("ENTER para continuar...", permitir_vacio=True)
                return
        except ValueError:
            print("❌ Calificación debe ser un número entero")
            pedir_texto("ENTER para continuar...", permitir_vacio=True)
            return

    nueva_evaluacion = {
        "cliente": doc_cliente,
        "instructor": doc_instructor,
        "fecha": fecha,
        "calificacion": pts_cliente,
    }

    citas.append(nueva_evaluacion)

    with open("data/evaluaciones.json", "w") as f:
        json.dump(citas, f, indent=4)

    print("✅ Evaluacion creada correctamente")
    pedir_texto("ENTER para continuar", permitir_vacio=True)
    
def listar_calificaciones_estudiante():

    doc_cliente = input("Ingrese el documento del cliente: ")

    try:
        with open("data/clientes.json", "r") as f:
            clientes = json.load(f)
    except:
        clientes = []

    try:
        with open("data/evaluaciones.json", "r") as f:
            evaluacion = json.load(f)
    except:
        evaluacion = []

    cliente = None
    for c in clientes:
        if str(c["documento"]) == doc_cliente:
            cliente = c
            break

    if cliente is None:
        print("❌ Cliente no existe")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    print(f"\n📋 Calificaciones de {cliente['nombre']}:\n")

    encontrado = False

    for e in evaluacion:
        if str(e["cliente"]) == doc_cliente:
            encontrado = True
            print(f"""
📅 Fecha: {e['fecha']}
👤 Cliente: {e ['cliente']}
👨‍🏫 Instructor: {e['instructor']}
📝 Calificacion: {e['calificacion']}
""")
            print("=="*15)

    if not encontrado:
        print("❌ Este cliente no tiene calificaciones registradas.")
    
    pedir_texto("ENTER para continuar...", permitir_vacio=True)

def promedio_calificaciones():
    try:
        with open("data/evaluaciones.json", "r") as f:
            evaluaciones = json.load(f)
    except:
        evaluaciones = []

    if not evaluaciones:
        print("No hay evaluaciones registradas.")
        pedir_texto("ENTER para continuar...", permitir_vacio=True)
        return

    total_calificaciones = sum(e['calificacion'] for e in evaluaciones)
    promedio = total_calificaciones / len(evaluaciones)

    print(f"📊 Promedio de calificaciones: {promedio: }")
    pedir_texto("ENTER para continuar...", permitir_vacio=True)