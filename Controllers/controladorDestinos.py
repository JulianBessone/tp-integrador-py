import tkinter as tk
from PIL import Image, ImageTk

class ControladorDestinos:
    def __init__(self, app, destinos):
        self.app = app
        self.marcadores = []
        self.destinos = destinos
        #self.cargar_marcadores()

    def cargar_marcadores(self):
        for ubicacion in self.app.ubicaciones:
            self.app.vista_destinos.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, texto='')
            marcador = (ubicacion.latitud, ubicacion.longitud)
            self.marcadores.append(marcador)
            # print(marcador)

    def id_ubicacion(self):
        pass


    def seleccionar_destinos(self, event):
        self.app.vista_destinos.desvincular_evento_seleccion()#Desvincular <<ListboxSelect>>
        #self.app.vista_destinos.marcadores.pop()
        indice_seleccionado = self.app.vista_destinos.destinos_listbox.curselection()
        indice_seleccionado = indice_seleccionado[0]
        destino_seleccionado = self.destinos[indice_seleccionado]
        self.app.vista_destinos.destino_seleccionado = destino_seleccionado
        self.app.vista_destinos.dibujar_destino_info()
        #self.app.vista_destinos.marcadores.append(destino_seleccionado)

        self.app.vista_destinos.mapa.delete_all_marker()

        for ubicacion in self.app.ubicaciones:
            if(destino_seleccionado.id_ubicacion == ubicacion.id):
                self.app.vista_destinos.mapa.set_position(ubicacion.latitud, ubicacion.longitud)
                self.app.vista_destinos.mapa.set_marker(ubicacion.latitud, ubicacion.longitud, text=f'{destino_seleccionado.nombre}')
                self.app.vista_destinos.mapa.set_zoom(16)#Cambiar a 16 si quieren
                self.cargar_marcadores()#Añado todos los demas marcadores.
        
        self.app.vista_destinos.vincular_evento_seleccion()#Vincular <<ListboxSelect>>

            # else:
            #     self.app.vista_destinos.mapa.delete_all_marker()
            #     self.app.vista_destinos.mapa.set_marker(ubicacion.latitud, ubicacion.longitud, text=f'{destino_seleccionado.nombre}')
        # print(self.app.vista_destinos.destino_seleccionado)

        # if self.app.vista_destinos.destinos_listbox.focus_get() == self.app.vista_destinos.destinos_listbox:
        #     self.app.vista_destinos.mapa.set_marker(ubicacion.latitud, ubicacion.longitud, text=f'{destino_seleccionado.nombre}')
        # else:
        #     self.app.vista_destinos.mapa.set_marker(ubicacion.latitud, ubicacion.longitud, text='')

        # def marcar_desmarcar_destinos(event):
        #     ind_destino = self.app.vista_destinos.destinos_listbox.curselection()
        #     ind_destino = ind_destino[0]
        #     select_destino = self.destinos[ind_destino]
        #     self.app.vista_destinos.select_destino = select_destino
        #     if ind_destino and self.app.vista_destino.destinos_listbox.focus_get == self.app.vista_destino.destinos_lisbox:
        #         self.app.vista_destinos.mapa.set_marker(text=f'{select_destino.nombre}')
        #     else:
        #         self.app.vista_destino.mapa.set_marker(text='')


    """def seleccionar_destinos_ubi(self, event):
        indice_seleccionado_ubi = self.app.vista_destinos.destinos_listbox.curselection()
        indice_seleccionado_ubi = indice_seleccionado_ubi[0]
        ubicacion_seleccionada = self.ubicaciones[indice_seleccionado_ubi]
        self.app.vista_destinos.ubicacion_seleccionada = ubicacion_seleccionada
        #Llamo a la función que me centre en los marcadores
    """
