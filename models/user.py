import json

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, historial_rutas=None):
        self.id = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = [] if historial_rutas is None else historial_rutas

    def agregar_ruta(self, id_ruta):
        self.historial_rutas.append(id_ruta)
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
        return [Usuario.de_json(json.dumps(dato)) for dato in datos]