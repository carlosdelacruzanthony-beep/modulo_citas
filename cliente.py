"""Módulo principal para la gestión y registro de clientes."""

class Cliente:  # pylint: disable=too-few-public-methods
    """Clase que representa a un cliente dentro del sistema."""

    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

        