import tkinter as tk
import customtkinter as ctk

# from tkinter import ttk
# from tkinter import messagebox
# from Views.resultadosBusquedaView import ResultadosBusquedaView


class InicioView(ctk.CTkFrame):
    def __init__(self, app, controladorInicio, destinos):
        super().__init__(app)
        self.app = app
        self.controlador = controladorInicio
        self.destinos = destinos
        


        # Colocar aquí el código para crear los widgets en este frame
        # Por ejemplo:
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para el texto "Food Travel App"
        self.label_titulo = ctk.CTkLabel(self, text="Food Travel App", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # Etiqueta para el input de búsqueda
        self.label_buscar = ctk.CTkLabel(self, text="Buscar restaurantes:")
        self.label_buscar.pack(pady=10)

        # Input para que el usuario busque restaurantes
        self.input_buscar = ctk.CTkEntry(self)
        self.input_buscar.pack()

        # Botón para realizar la búsqueda
        self.boton_buscar = ctk.CTkButton(
    self,
    text="Buscar",
    width=200,  # Ajustar el ancho del botón
    height=30,  # Ajustar la altura del botón
    command=lambda: self.controlador.buscar_restaurantes(
        self.input_buscar.get()
            ),
        )
        self.boton_buscar.place(x=340, y=130)
        #self.boton_buscar.pack(pady=5)


        # Botones: Destinos, Reviews y Planificar Visita


        self.boton_destinos = ctk.CTkButton(
            self,
            text="Destinos",
            width=200,
            height=40,
            command=lambda: self.controlador.mostrar_destinos())#Falta el controlador

        self.boton_destinos.place(x=40, y=170) 
        #self.boton_destinos.pack(pady=5)

        self.boton_reviews = ctk.CTkButton(
            self,
            text="Reviews",
            width=200,
            height=40,
            command=lambda: self.controlador.mostrar_reviews()
        )
        self.boton_reviews.place(x=340, y=170) 
        #self.boton_reviews.pack(pady=5)


        self.boton_planificar_visita = ctk.CTkButton(self,
        text="Planificar Visita",
        width=200,
        height=40,
        command= lambda: self.controlador.mostrar_rutas())
        self.boton_planificar_visita.place(x=640, y=170)
        #self.boton_planificar_visita.pack(pady=5)

        # Mostrar los destinos en una etiqueta
        self.label_destinos = ctk.CTkLabel(self, text="Destinos:")
        self.label_destinos.place(x=300, y=220)
        #self.label_destinos.pack()

        destinos_text = "\n".join([f"- {destino.nombre}" for destino in self.destinos])
        self.reviews_label = ctk.CTkLabel(self, text=destinos_text, justify=tk.LEFT)
        self.reviews_label.place(x=300, y=250)
        #self.reviews_label.pack()
