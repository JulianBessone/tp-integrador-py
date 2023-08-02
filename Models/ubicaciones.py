import json

class Ubicacion:
    def __init__(self, id_ubicacion, direccion, latitud, longitud):
        self.id = id_ubicacion
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return f"Ubicación {self.id}: {self.direccion}, Coordenadas: {self.coordenadas}"
    def a_json(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        id_ubicacion = datos.pop('id_ubicacion', None)
        direccion = datos.pop('direccion', None)
        coordenadas = datos.pop('coordenadas', None)
        latitud, longitud = [float(coord.strip()) for coord in coordenadas.split(",")]
        return cls(id_ubicacion, direccion, latitud, longitud)
    
    @staticmethod
    def cargar_ubicaciones(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Ubicacion.de_json(json.dumps(dato)) for dato in datos]