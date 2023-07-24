from utils import usuarios_a_json

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, historial_rutas=None):
        self.id = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = [] if historial_rutas is None else historial_rutas

    def agregar_ruta(self, id_ruta):
        self.historial_rutas.append(id_ruta)

usuario1 = Usuario(1, "Juan", "Pérez")
usuario2 = Usuario(2, "Nicolas", "Fernandez")
usuario3 = Usuario(3, "David", "Costilla")
usuario4 = Usuario(4, "Franco", "Acosta")
usuario5 = Usuario(5, "Camila", "Galli")
usuario6 = Usuario(6, "Abigail", "Nieva")

usersLista = (usuario1,usuario2,usuario3,usuario4,usuario5,usuario6)

usersListaJSON = usuarios_a_json(usersLista)
print(usersListaJSON)