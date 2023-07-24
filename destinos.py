from utils import objetos_a_json

class DestinoCulinario:
    def __init__(self, id_destino, nombre, tipo_cocina, ingredientes, precio_minimo,
                 precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen):
        self.id = id_destino
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    def __str__(self):
        return f"Destino Culinario: {self.nombre}, Tipo de cocina: {self.tipo_cocina}, " \
               f"Popularidad: {self.popularidad}, Disponibilidad: {self.disponibilidad}"

    def cambiar_disponibilidad(self, disponibilidad_nueva):
        self.disponibilidad = disponibilidad_nueva

# Ejemplo de uso
destino1 = DestinoCulinario(1, "Restaurante Italiano", "Italiana",
                            ["pasta", "pizza", "tiramisú"], 20, 50, 4.5, True,
                            "ubicacion_1", "https://example.com/imagen1.jpg")

destino2 = DestinoCulinario(2, "Comida Mediterránea", "Mediterránea",
                            ["aceitunas", "pescado", "ensaladas"], 25, 60, 4.2, False,
                            "ubicacion_2", "https://example.com/imagen2.jpg")

destino3 = DestinoCulinario(3, "Restaurante Hindú", "Hindú",
                            ["curry", "samosa", "naan"], 15, 40, 4.7, True,
                            "ubicacion_3", "https://example.com/imagen3.jpg")

destino4 = DestinoCulinario(4, "Comida Regional", "Regional",
                            ["asado", "empanadas", "locro"], 18, 55, 4.0, True,
                            "ubicacion_4", "https://example.com/imagen4.jpg")

listaDestinos = (destino1,destino2,destino3,destino4)

listaDestinosJSON = objetos_a_json(listaDestinos)