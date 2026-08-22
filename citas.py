
citas_programadas = []

def agendar_cita(paciente, fecha, hora):
    nueva_cita = {"paciente": paciente, "fecha": fecha, "hora": hora}
    citas_programadas.append(nueva_cita)
    print(f"Cita agendada para {paciente}")

def cancelar_cita(paciente):
    global citas_programadas
    citas_programadas = [c for c in citas_programadas if c["paciente"] != paciente]
    print(f"Citas de {paciente} canceladas.")