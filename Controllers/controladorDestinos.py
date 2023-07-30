import tkinter as tk

class ControladorDestinos:
    def __init__(self, app, destinos):
        self.app = app
        self.marcadores = []
        self.destinos = destinos
        #self.cargar_marcadores()

    def cargar_marcadores(self):
        for ubicacion in (self.app.ubicaciones):
            self.app.vista_destinos.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud)
            marcador = (ubicacion.latitud, ubicacion.longitud)
            self.marcadores.append(marcador)
            print(marcador)

    def id_ubicacion(self):
        pass


    def seleccionar_destinos(self, event):
        #self.app.vista_destinos.marcadores.pop()
        indice_seleccionado = self.app.vista_destinos.destinos_listbox.curselection()
        indice_seleccionado = indice_seleccionado[0]
        destino_seleccionado = self.destinos[indice_seleccionado]
        self.app.vista_destinos.destino_seleccionado = destino_seleccionado
        self.app.vista_destinos.dibujar_destino_info()
        #self.app.vista_destinos.marcadores.append(destino_seleccionado)
        for ubicacion in self.app.ubicaciones:
            if(destino_seleccionado.id_ubicacion == ubicacion.id):
                self.app.vista_destinos.mapa.set_position(ubicacion.latitud, ubicacion.longitud)
                self.app.vista_destinos.mapa.set_marker(ubicacion.latitud, ubicacion.longitud, text= f'{destino_seleccionado.nombre}')
                self.app.vista_destinos.mapa.set_zoom(16)
        print(self.app.vista_destinos.destino_seleccionado)

    """def seleccionar_destinos_ubi(self, event):
        indice_seleccionado_ubi = self.app.vista_destinos.destinos_listbox.curselection()
        indice_seleccionado_ubi = indice_seleccionado_ubi[0]
        ubicacion_seleccionada = self.ubicaciones[indice_seleccionado_ubi]
        self.app.vista_destinos.ubicacion_seleccionada = ubicacion_seleccionada
        #Llamo a la función que me centre en los marcadores
    """
