def mostrar_logo():
    print("""
██████╗ ██████╗ ██╗██╗   ██╗███████╗   ███████╗ █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██║██║   ██║██╔════╝   ██╔════╝██╔══██╗██╔════╝██╔════╝
██║  ██║██████╔╝██║██║   ██║█████╗     ███████╗███████║█████╗  █████╗  
██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝     ╚════██║██╔══██║██╔══╝  ██╔══╝  
██████╔╝██║  ██║██║ ╚████╔╝ ███████╗   ███████║██║  ██║██║     ███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝
""")

def pedir_opcion():
    print("""
                ╔══════════════════════════════════════╗
                ║     INGRESE LA OPCIÓN DESEADA        ║
                ╠══════════════════════════════════════╣
                ║  [1] Gestionar Clientes              ║
                ║  [2] Gestionar Instructores          ║
                ║  [3] Gestionar Vehiculos             ║
                ║  [4] Gestionar Citas                 ║
                ║  [5] Reportes / Historial            ║
                ║  [6] Salir                           ║
                ╠══════════════════════════════════════╣""")

    opc = int(input("                ║  Opción: "))

    print("                ╚══════════════════════════════════════╝")
    return opc

def pedir_opcion_clientes():
    print("""
                ╔══════════════════════════════════════╗
                ║         GESTIONAR CLIENTES           ║
                ╠══════════════════════════════════════╣
                ║  [1] Registrar cliente               ║
                ║  [2] Listar clientes                 ║
                ║  [3] Buscar cliente                  ║
                ║  [4] Menu principal                  ║
                ╠══════════════════════════════════════╣""")

    opc = int(input("                ║  Opción: "))

    print("                ╚══════════════════════════════════════╝")
    return opc

def pedir_opcion_instructores():
    print("""
                ╔══════════════════════════════════════╗
                ║        GESTIONAR INSTRUCTORES        ║
                ╠══════════════════════════════════════╣
                ║  [1] Registrar instructor            ║
                ║  [2] Listar instructores             ║
                ║  [3] Menu principal                  ║
                ╠══════════════════════════════════════╣""")

    opc = int(input("                ║  Opción: "))

    print("                ╚══════════════════════════════════════╝")
    return opc
    
def pedir_opcion_vehiculos():
    print("""
                ╔══════════════════════════════════════╗
                ║         GESTIONAR VEHICULOS          ║
                ╠══════════════════════════════════════╣
                ║  [1] Registrar vehículo              ║
                ║  [2] Listar vehículos                ║
                ║  [3] Cambiar disponibilidad          ║
                ║  [4] Menu principal                  ║
                ╠══════════════════════════════════════╣""")

    opc = int(input("                ║  Opción: "))

    print("                ╚══════════════════════════════════════╝")
    return opc

def pedir_opcion_citas():
    print("""
                ╔══════════════════════════════════════╗
                ║           GESTIONAR CITAS            ║
                ╠══════════════════════════════════════╣
                ║  [1] Programar cita                  ║
                ║  [2] Ver citas                       ║
                ║  [3] Buscar por cliente              ║
                ║  [4] Buscar por fecha                ║
                ║  [5] Registrar asistencia            ║
                ║  [6] Menu principal                  ║
                ╠══════════════════════════════════════╣""")

    opc = int(input("                ║  Opción: "))

    print("                ╚══════════════════════════════════════╝")
    return opc

def pedir_opcion_reporte():
    print("""
                ╔══════════════════════════════════════╗
                ║           GESTIONAR CITAS            ║
                ╠══════════════════════════════════════╣
                ║  [1] Historial por cliente           ║
                ║  [2] Menu principal                  ║
                ╠══════════════════════════════════════╣""")

    opc = int(input("                ║  Opción: "))

    print("                ╚══════════════════════════════════════╝")
    return opc