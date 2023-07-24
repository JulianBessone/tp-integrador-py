import json

class RutaVisita:
    def __init__(self, id_ruta, nombre, destinos):
        self.id = id_ruta
        self.nombre = nombre
        self.destinos = destinos

    def __str__(self):
        return f"Ruta de Visita: {self.nombre}, ID: {self.id}, Destinos: {self.destinos}"
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
        return [RutaVisita.de_json(json.dumps(dato)) for dato in datos]



