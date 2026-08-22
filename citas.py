
citas_programadas = []

def agendar_cita(paciente, fecha, hora):
    nueva_cita = {"paciente": paciente, "fecha": fecha, "hora": hora}
    citas_programadas.append(nueva_cita)
    print(f"Cita agendada para {paciente}")