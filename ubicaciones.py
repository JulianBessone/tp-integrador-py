from utils import objetos_a_json

class Ubicacion:
    def __init__(self, id_ubicacion, direccion, coordenadas):
        self.id = id_ubicacion
        self.direccion = direccion
        self.coordenadas = coordenadas

    def __str__(self):
        return f"Ubicación {self.id}: {self.direccion}, Coordenadas: {self.coordenadas}"

ubicacion1 = Ubicacion(1, "Plaza Mayor, Madrid", [40.4155, -3.7079])
ubicacion2 = Ubicacion(2, "Central Park, New York", [40.7829, -73.9654])
ubicacion3 = Ubicacion(3, "Torre Eiffel, Paris", [48.8584, 2.2945])
ubicacion4 = Ubicacion(4, "Calle Principal Número 123", [37.7749, -122.4194])
ubicacion5 = Ubicacion(5, "Puerto de Sydney", (33.8688, 151.2093))
ubicacion6 = Ubicacion(6, "Gran Muralla China", [40.4319, 116.5704])

listaUbicaciones = (ubicacion1,ubicacion2,ubicacion3,ubicacion4,ubicacion5,ubicacion6)
listaUbicacionesJSON = objetos_a_json(listaUbicaciones)


