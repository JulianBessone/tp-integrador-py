class ControladorActividades:
    def __init__(self, app, destinos, actividades):
        self.app = app
        self.destinos = destinos
        self.actividades = actividades  #aca paso la lista de objetos de todas las actividades


    def regresar_destinos(self):
        self.app.cambiar_frame(self.app.vista_destinos)

    def obtener_actividades(self):

        return self.actividades  #devuelvo la lista de actividades como objetos

    def obtener_actividades_destino(self, indice):
        actividades_por_destino = []
        for actividad in self.actividades: #modelo_actividad tiene la lista de todas las actividades 
            if actividad.destino_id == indice:
                actividades_por_destino.append(actividad)
        return actividades_por_destino  



