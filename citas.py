
citas_programadas = []

def agendar_cita(paciente, fecha, hora):
    nueva_cita = {"paciente": paciente, "fecha": fecha, "hora": hora}
    citas_programadas.append(nueva_cita)
    print(f"Cita agendada para {paciente}")

def cancelar_cita(paciente):
    global citas_programadas
    citas_programadas = [c for c in citas_programadas if c["paciente"] != paciente]
    print(f"Citas de {paciente} canceladas.")

def reprogramar_cita(paciente):
    cita_encontrada = False
    for cita in citas_programadas:
        if cita["paciente"] == paciente:
            cita["fecha"] = nueva_fecha
            cita["hora"] = nueva_hora
            cita_encontrada = True
            print(f"Cita de {paciente} reprogramada para el {nueva_fecha} a las {nueva_hora}.")
            break  # Remueve el break si un paciente puede tener múltiples citas y quieres cambiarlas todas.
            
    if not cita_encontrada:
        print(f"No se encontró ninguna cita programada para {paciente}.")