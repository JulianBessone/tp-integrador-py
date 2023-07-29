class ControladorDestinos:
    def __init__(self, app, destinos):
        self.app = app
        self.destinos = destinos #aca paso la lista de objetos destino

    def obtener_destinos(self):
        return self.destinos  #devuelvo la lista de destinos

    def seleccionar_destino(self):
        """
        Obtiene el índice del destino seleccionado y llama a la vista de
        información para mostrar la información de la actividad.
        """
        indice = self.app.vista_destinos.obtener_destino_seleccionado()
        if indice is not None:
            destino = self.destinos[indice]  #selecciono el objeto de la lista de objetos
            self.app.vista_actividades.mostrar_actividades_destino(destino)
            self.app.cambiar_frame(self.app.vista_actividades)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
