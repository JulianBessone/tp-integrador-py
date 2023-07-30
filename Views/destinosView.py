#Importamos tkinter con el alias tk:
import tkinter as tk
from tkintermapview import TkinterMapView
""" #Impotamos Themes Tkinter:
from tkinter import ttk

#Importamos TkinterMapView(para el mapa):
from tkintermapview import TkinterMapView

#Importamos Image y ImageTk de la libreria PIL(para las imagenes):
from PIL import Image, ImageTk """



#Clase principal de la vista:
class DestinosView(tk.Frame):

    #Método constructor:
    def __init__(self, app, controlador, destinos, ubicaciones):
        super().__init__(app)
        self.app = app
        self.controlador = controlador
        self.destinos = destinos
        self.ubicaciones = ubicaciones

        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Destinos")
        self.app.geometry("800x600")

        self.create_widgets()
    
    def create_widgets(self):

        self.label_titulo = tk.Label(self, text="Destinos", font=("Arial", 20))
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.destinos_listbox = tk.Listbox(self, width=40, height=20)

        for destino in self.destinos:
            """Deberias pasar por parametro la lista de destinos y luego dentro de este for buscar el destino correspondienta a id_destino del review"""
            self.destinos_listbox.insert(tk.END, destino.nombre)

        self.destinos_listbox.grid(row=1, column=0, padx=10, pady=10)

        ##MAPA VISTA
        self.mapa = TkinterMapView(self, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.grid(row=1, column=1, padx=10, pady=10)

        ##AGREGAR MARCADORES DE DESTINOS
    def agregar_marcador_mapa(self, latitud, longitud, texto):
        return self.mapa.set_marker(latitud, longitud, text=texto)


