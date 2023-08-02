
#Importamos tkinter con el alias tk:
import tkinter as tk
from tkintermapview import TkinterMapView
""" #Impotamos Themes Tkinter:
from tkinter import ttk

#Importamos TkinterMapView(para el mapa):
from tkintermapview import TkinterMapView

#Importamos Image y ImageTk de la libreria PIL(para las imagenes):
from PIL import Image, ImageTk """
from PIL import Image, ImageTk



#Clase principal de la vista:
class DestinosView(tk.Frame):

    #Método constructor:
    def __init__(self, app, controlador, destinos, ubicaciones):
        super().__init__(app)
        self.app = app
        self.controlador = controlador
        self.destinos = destinos
        self.ubicaciones = ubicaciones
        self.marcadores = ubicaciones
        self.destino_seleccionado = {}

        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Destinos")
        self.app.geometry("885x620")
        self.app.resizable(1, 1)

        self.create_widgets()
        

    def desvincular_evento_seleccion(self):
        self.destinos_listbox.unbind('<<ListboxSelect>>')

    def vincular_evento_seleccion(self):
        self.destinos_listbox.bind('<<ListboxSelect>>', self.controlador.seleccionar_destinos)
    
    def create_widgets(self):

        ##AQUI CREO LA LISTA DE DESTINOS
        self.destinos_listbox = tk.Listbox(self, width=40, height=16)

        for destino in self.destinos:
            """Deberias pasar por parametro la lista de destinos y luego dentro de este for buscar el destino correspondienta a id_destino del review"""
            self.destinos_listbox.insert(tk.END, destino.nombre)

        self.destinos_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        self.destinos_listbox.bind('<<ListboxSelect>>', self.controlador.seleccionar_destinos)
        self.destinos_listbox.bind("<Double-Button-1>", self.seleccionar_destino)
        # self.destinos_listbox.bind('<<ListboxSelect>>', self.controlador.seleccionar_destinos_ubi)

        buttom_volver = tk.Button(self, text='Volver', command=lambda:self.controlador.mostrar_inicio())
        buttom_volver.config(width=27, height=2)
        buttom_volver.place(x=27 ,y=560)

        ##MAPA VISTA
        self.mapa = TkinterMapView(self, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(14)
        self.mapa.grid(row=0, column=1, padx=10, pady=10, sticky="nsew",rowspan=2)
        self.mapa.set_marker(-24.77616437851034, -65.41079411004006)

        for ubicacion in (self.marcadores):
            self.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, '')
        


        ##AGREGAR MARCADORES DE DESTINOS
    def agregar_marcador_mapa(self, latitud, longitud, texto):
        return self.mapa.set_marker(latitud, longitud, text=texto)

    def dibujar_destino_info(self):

        self.tituloDetalleDestino = tk.Label(self, text='INFORMACIÓN DEL DESTINO')
        self.tituloDetalleDestino.config(width=30, height=3, pady=0)
        self.tituloDetalleDestino.place(x=10, y=480)


        self.textoDisponiblidad = tk.Label(self, width=30, height=1)
        if self.destino_seleccionado.disponibilidad == 1:
            self.textoDisponiblidad.config(text='Abierto')
        else:
            self.textoDisponiblidad.config(text='Cerrado')
        self.textoDisponiblidad.place(x=20, y=510)
        self.textoPopularidad = tk.Label(self, width=30, height=1)
        self.textoPopularidad.config(text=f'{self.destino_seleccionado.popularidad}')
        self.textoPopularidad.place(x=20, y=530)
        

    def obtener_destino_seleccionado(self):
        """
        Retorna el índice del destino seleccionado en la lista.
        """
        indice = self.destinos_listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_destino(self, event):
        """
        Obtiene el índice del destinoS seleccionado y llama al controlador para
        mostrar la información del destino.
        """
        self.controlador.seleccionar_destino()