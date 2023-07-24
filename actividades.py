from utils import objetos_a_json

class Actividad:
    def __init__(self, id_actividad, nombre, destino_id, hora_inicio):
        self.id = id_actividad
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    def __str__(self):
        return f"Actividad: {self.nombre}, ID: {self.id}, Destino ID: {self.destino_id}, Hora de inicio: {self.hora_inicio}"

# Ejemplo de uso
actividad1 = Actividad(1, "Espectáculo de Flamenco", 2, "2023-07-04T20:30:00")
actividad2 = Actividad(2, "Tour de Vinos", 1, "2023-07-05T14:00:00")
actividad3 = Actividad(3, "Recital de Jazz", 3, "2023-07-06T19:30:00")
actividad4 = Actividad(4, "Visita Guiada a Museo", 1, "2023-07-05T10:00:00")

listaActividades = (actividad1,actividad2,actividad3,actividad4)
listaActividadesJSON = objetos_a_json(listaActividades)
