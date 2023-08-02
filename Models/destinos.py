import json

class DestinoCulinario:
    def __init__(self, id_destino, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen):
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

    #def __str__(self):
    #    return f"Destino Culinario: {self.nombre}, Tipo de cocina: {self.tipo_cocina}, \nPopularidad: {self.popularidad}, Disponibilidad: {self.disponibilidad}" 

    def cambiar_disponibilidad(self, disponibilidad_nueva):
        self.disponibilidad = disponibilidad_nueva
    def a_json(self):
        return json.dumps(self.__dict__)
    
    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    def cargar_destinos(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [DestinoCulinario.de_json(json.dumps(dato)) for dato in datos]