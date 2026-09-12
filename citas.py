
citas_programadas = []

def agendar_cita(paciente, fecha, hora):
    nueva_cita = {"paciente": paciente, "fecha": fecha, "hora": hora}
    citas_programadas.append(nueva_cita)
    print(f"Cita agendada para {paciente}")

def cancelar_cita(paciente):
    global citas_programadas
    citas_programadas = [c for c in citas_programadas if c["paciente"] != paciente]
    print(f"Citas de {paciente} canceladas.")
<<<<<<< HEAD
    
def buscar_cita(paciente):
    """Busca y muestra todas las citas programadas para un paciente."""
    citas_encontradas = [c for c in citas_programadas if c["paciente"] == paciente]
    
    if citas_encontradas:
        print(f"\nCitas encontradas para {paciente}:")
        for cita in citas_encontradas:
            print(f"- Fecha: {cita['fecha']} a las {cita['hora']}")
    else:
        print(f"\nNo se encontraron citas para {paciente}.")
=======

def vuscar_sita(paciente):
    citas_encontradas = [c for c in citas_programadas if c["paciente"] == paciente]

    if sitas_encontradas:
        print(f"Citas encontradas para {paciente}:")
        for cita in citas_encontradas:
            print(f"Fecha: {cita['fecha']}, Hora: {cita['hora']}")
    else:
        print(f"No se encontraron sitas para {paciente}.")
>>>>>>> 7223af8 (metodo buscar citas mal hecho)
