import json


class Usuario:
    def __init__(self, id_usuario, nombre, apellido, historial_rutas=None):
        if not isinstance(id_usuario, int):
            print("El id de usuario debe ser un numero")
        if not isinstance(nombre, str):
            print(
                "El nombre no es valido, recuerda que solo debe ser una cadena de texto"
            )
        if not isinstance(apellido, str):
            print(
                "El apellido no es valido, recuerda que solo debe ser una cadena de texto"
            )

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
    def cargar_users(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return [Usuario.de_json(json.dumps(dato)) for dato in datos]
