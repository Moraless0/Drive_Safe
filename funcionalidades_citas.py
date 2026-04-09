import json, os

def programar_cita():
    os.system("clear")

    documento = input("Documento del cliente: ").strip()
    instructor_id = input("ID del instructor: ").strip()
    placa = input("Placa del vehículo: ").strip().upper()
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    hora = input("Hora (HH:MM): ").strip()
    duracion = input("Duración (minutos): ").strip()

    try:
        with open("clientes.json", "r") as f:
            clientes = json.load(f)

        with open("instructores.json", "r") as f:
            instructores = json.load(f)

        with open("vehiculos.json", "r") as f:
            vehiculos = json.load(f)

        try:
            with open("citas.json", "r") as f:
                citas = json.load(f)
        except:
            citas = []

    except:
        print("❌ Error cargando archivos")
        input("ENTER para continuar...")
        return

    # 🔍 3. VALIDAR CLIENTE
    cliente_existe = False
    for c in clientes:
        if c["documento"] == documento:
            cliente_existe = True
            break

    if not cliente_existe:
        print("❌ Cliente no existe")
        return

    # 🔍 4. VALIDAR INSTRUCTOR
    instructor_encontrado = None
    for i in instructores:
        if str(i["id"]) == instructor_id:
            instructor_encontrado = i
            break

    if not instructor_encontrado:
        print("❌ Instructor no existe")
        return

    # 🔍 5. VALIDAR VEHÍCULO
    vehiculo_encontrado = None
    for v in vehiculos:
        if v["placa"] == placa:
            vehiculo_encontrado = v
            break

    if not vehiculo_encontrado:
        print("❌ Vehículo no existe")
        return

    # 🔥 6. VALIDAR DISPONIBILIDAD
    if not vehiculo_encontrado["disponible"]:
        print("❌ Vehículo no disponible")
        return

    # 🔥 7. VALIDAR COMPATIBILIDAD
    if vehiculo_encontrado["tipo"] != instructor_encontrado["especialidad"]:
        print("❌ Instructor no compatible con el vehículo")
        return

    # 🔥 8. EVITAR MISMA HORA (PRO)
    for cita in citas:
        if cita["fecha"] == fecha and cita["hora"] == hora:
            print("❌ Ya existe una cita en ese horario")
            return

    # 🔢 9. GENERAR ID
    if citas:
        nuevo_id = citas[-1]["id"] + 1
    else:
        nuevo_id = 1

    # 🧾 10. CREAR CITA
    nueva_cita = {
        "id": nuevo_id,
        "cliente": documento,
        "instructor": instructor_id,
        "vehiculo": placa,
        "fecha": fecha,
        "hora": hora,
        "duracion": duracion,
        "asistencia": None,
        "observaciones": ""
    }

    # 💾 11. GUARDAR
    citas.append(nueva_cita)

    with open("citas.json", "w") as f:
        json.dump(citas, f, indent=4)

    print("✅ Cita programada correctamente")
    input("ENTER para continuar...")