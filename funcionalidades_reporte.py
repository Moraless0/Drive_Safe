from utilidades import pedir_texto
import json, os

def menu_historial():

    os.system("clear")

    try:
        with open("data/citas.json", "r") as f:
            citas = json.load(f)
    except:
        citas = []

    total_citas = len(citas)

    clientes_unicos = set()
    fechas_unicas = set()
    con_asistencia = 0
    sin_asistencia = 0

    for c in citas:
        clientes_unicos.add(c["cliente"])
        fechas_unicas.add(c["fecha"])

        if c["asistencia"]:
            con_asistencia += 1
        else:
            sin_asistencia += 1

    print(f"""
============ MENÚ DE HISTORIAL =========

   1. 📋 Todas las citas .......... {total_citas}
   2. 👤 Citas por cliente ........ {len(clientes_unicos)}
   3. 📅 Citas por fecha .......... {len(fechas_unicas)}
   4. ✅ Con asistencia ........... {con_asistencia}
   5. ❌ Sin asistencia ........... {sin_asistencia}

========================================
""")

    pedir_texto("ENTER para continuar", permitir_vacio=True)