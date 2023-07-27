import json

class Ubicacion:
    def __init__(self, id_ubicacion, direccion, coordenadas):
        self.id = id_ubicacion
        self.direccion = direccion
        self.coordenadas = coordenadas

    def __str__(self):
        return f"Ubicación {self.id}: {self.direccion}, Coordenadas: {self.coordenadas}"
    def a_json(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_reviews(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Ubicacion.de_json(json.dumps(dato)) for dato in datos]