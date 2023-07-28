#Importamos tkinter con el alias tk:
import tkinter as tk

""" #Impotamos Themes Tkinter:
from tkinter import ttk

#Importamos TkinterMapView(para el mapa):
from tkintermapview import TkinterMapView

#Importamos Image y ImageTk de la libreria PIL(para las imagenes):
from PIL import Image, ImageTk """



#Clase principal de la vista:
class DestinosView(tk.Frame):

    #Método constructor:
    def __init__(self, app, seleccionar_destino_callback=None, seleccionar_ubicacion_callback=None):
        super().__init__(app)
        self.app = app
