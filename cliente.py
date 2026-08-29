class Cliente:
    def __init__(self, id_cliente, nombre, telefono, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def obtener_informacion(self):
        """Retorna una cadena con el resumen de los datos del cliente."""
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Tel: {self.telefono} | Correo: {self.correo}"

    def actualizar_contacto(self, nuevo_telefono=None, nuevo_correo=None):
        """Permite actualizar el teléfono y/o correo del cliente."""
        if nuevo_telefono:
            self.telefono = nuevo_telefono
        if nuevo_correo:
            self.correo = nuevo_correo
        print(f"Datos de contacto actualizados para {self.nombre}.")


# Lista global para gestionar los clientes registrados
lista_clientes = []

def registrar_cliente(id_cliente, nombre, telefono, correo):
    """Crea una nueva instancia de Cliente y la guarda en la lista."""
    for c in lista_clientes:
        if c.id_cliente == id_cliente:
            print(f"El cliente con ID {id_cliente} ya existe.")
            return None
            
    nuevo_cliente = Cliente(id_cliente, nombre, telefono, correo)
    lista_clientes.append(nuevo_cliente)
    print(f"Cliente '{nombre}' registrado con éxito.")
    return nuevo_cliente

def buscar_cliente(id_cliente):
    """Busca a un cliente en la lista por su ID."""
    for c in lista_clientes:
        if c.id_cliente == id_cliente:
            return c
    print(f"Cliente con ID {id_cliente} no encontrado.")
    return None