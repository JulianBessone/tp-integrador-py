import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class ControladorDestinos:
    def __init__(self, app, destinos):
        self.app = app
        #self.marcadores = []
        self.destinos = destinos
        #self.cargar_marcadores()
        self.imagen_tk = None

    def cargar_marcadores(self):
        for ubicacion in self.app.ubicaciones:
            self.app.vista_destinos.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, texto='')
            #marcador = (ubicacion.latitud, ubicacion.longitud)
            #self.marcadores.append(marcador)
            # print(marcador)

    def seleccionar_destinos(self, event):
        self.imagen_tk = None
        self.app.vista_destinos.desvincular_evento_seleccion()#Desvincular <<ListboxSelect>>
        indice_seleccionado = self.app.vista_destinos.destinos_listbox.curselection()
        indice_seleccionado = indice_seleccionado[0]
        destino_seleccionado = self.destinos[indice_seleccionado]
        self.app.vista_destinos.destino_seleccionado = destino_seleccionado
        self.app.vista_destinos.dibujar_destino_info()

        self.app.vista_destinos.mapa.delete_all_marker()

        for ubicacion in self.app.ubicaciones:
            if(destino_seleccionado.id_ubicacion == ubicacion.id):
                self.app.vista_destinos.mapa.set_position(ubicacion.latitud, ubicacion.longitud)
                self.app.vista_destinos.mapa.set_marker(ubicacion.latitud, ubicacion.longitud, text=f'{destino_seleccionado.nombre}')
                self.app.vista_destinos.mapa.set_zoom(14)#Cambiar a 16 si quieren
                self.cargar_marcadores()#Añado todos los demas marcadores.
        
        if self.imagen_tk is None:
            rutaIMG = f'assets/img/{destino_seleccionado.imagen}'
            imagen_pil = Image.open(f"assets/img/{destino_seleccionado.imagen}")
            self.imagen_tk = ImageTk.PhotoImage(imagen_pil)
        etiqueta_imagen = tk.Label(self.app.vista_destinos, image=self.imagen_tk)
        etiqueta_imagen.config(width=240, height=200)
        etiqueta_imagen.place(x=12, y=325)

        self.app.vista_destinos.vincular_evento_seleccion()#Vincular <<ListboxSelect>>


    def seleccionar_destino(self):
        """
        Obtiene el índice del destino seleccionado y llama a la vista de
        información para mostrar la información de la actividad.
        """

        indice = self.app.vista_destinos.obtener_destino_seleccionado()
        if indice is not None:
            destino = self.destinos[indice]  #selecciono el objeto de la lista de objetos
            self.app.vista_actividades.mostrar_actividades_destino(destino)
            ##self.imagen_tk = '' ## ---(!!Corrección)--- Borraremos la imagen porque por alguna razon se superpone al cambiar de vista

            self.app.cambiar_frame(self.app.vista_actividades)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def mostrar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)