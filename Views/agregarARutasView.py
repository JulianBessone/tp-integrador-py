from tkinter import Frame, Label, Grid, N, S, E, W
import tkinter as tk
from datetime import datetime


class AgregarARutasView(tk.Frame):
    def __init__(self, app, controladorRutas, destinos, rutas):
        super().__init__(app)
        self.app = app
        self.controlador = controladorRutas
        self.destinos = destinos
        self.rutas = rutas


        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Agrega el destino a tu ruta")
        self.app.geometry("885x620")
        self.app.resizable(1, 1)

        self.create_widgets()


    def create_widgets(self): 
        self.titulo = tk.Label(self, text="Agrega el destino a tu ruta", font=("Arial", 20))
        self.titulo.place(x=200,y=20)

        self.rutas_label = tk.Label(self, text="Selecciona la ruta", font=("Arial", 14))
        self.rutas_label.place(x=10,y=70)

        #muestro la lista de las ruts
        self.rutas_listbox = tk.Listbox(self, width=40, height=16)

        for ruta in self.rutas:
            """Deberias pasar por parametro la lista de destinos y luego dentro de este for buscar el destino correspondienta a id_destino del review"""
            self.rutas_listbox.insert(tk.END, ruta.nombre)

        self.rutas_listbox.place(x=10, y=100)
        self.rutas_listbox.bind('<<ListboxSelect>>', self.controlador.seleccionar_ruta)

        # Crea el botón "Guardar" y lo agrega al contenedor
        self.boton_agregar_destino = tk.Button(
            self, 
            text="Agregar el destino", 
            command=lambda: self.controlador.agregar_destino()
        )

        self.boton_agregar_destino.place(x=50, y=400)        


