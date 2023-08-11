import json
import os

class RutaDeVisita:
    def __init__(self, id_ruta, nombre_ruta, destinos):
        self.id = id_ruta
        self.nombre = nombre_ruta
        self.destinos = destinos

    def __str__(self):
        return f"Ruta {self.id}: Nombre: {self.nombre}"


    def a_json(self):
        """
        Convierte el objeto RutaDeVisita a formato JSON.
        """
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        """
        Crea un objeto RutaDeVisita a partir de un JSON.
        """
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_rutas(archivo_json):
        """
        Carga una lista de rutas desde un archivo JSON.
        """
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [RutaDeVisita.de_json(json.dumps(dato)) for dato in datos]




    # def cargar_rutas(self, archivo_json):
    #     ruta_archivo = os.path.join("data", archivo_json)
    #     with open(archivo_json, "r") as archivo:
    #         datos = json.load(archivo)
    #     self.rutas = [RutaDeVisita(**dato) for dato in datos]


