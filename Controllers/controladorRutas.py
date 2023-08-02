from Models.rutasVisitas import RutaDeVisita

class ControladorRutas:
    def __init__(self, app, destinos, rutas, actividades):
        self.app = app
        self.destinos = destinos #aca paso la lista de objetos destino
        self.rutas = rutas #paso la lista de las rutas.
        self.actividades = actividades #paso la lista de las actividades.
       

    def obtener_destinos(self):
        return self.destinos  #devuelvo la lista de destinos

    def obtener_rutas(self):
        return self.rutas  #devuelvo la lista de rutas        

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)


    def agregar_ruta(self, nombre_ruta, ventana_nueva_ruta=None):
        if nombre_ruta:
            # Obtener el siguiente id disponible para la nueva ruta
            nuevo_id_ruta = len(self.rutas) + 1

            # Crear una nueva instancia de RutaDeVisita y agregarla a la lista de rutas
            nueva_ruta = RutaDeVisita(nuevo_id_ruta, nombre_ruta, [])
            self.rutas.append(nueva_ruta)

            # Si se proporciona una ventana Toplevel, ocultarla
            if ventana_nueva_ruta:
                ventana_nueva_ruta.destroy()

            return self.rutas


    # def seleccionar_destino(self):
    #     """
    #     Obtiene el índice del destino seleccionado y llama a la vista de
    #     información para mostrar la información de la actividad.
    #     """
    #     indice = self.app.vista_rutas.obtener_destino_seleccionado()
    #     if indice is not None:
    #         destino = self.destinos[indice]  #selecciono el objeto de la lista de objetos
    #         self.app.vista_actividades.mostrar_actividades_destino(destino) #paso el objeto a mostrar_actividades_destino
    #         self.app.cambiar_frame(self.app.vista_actividades)