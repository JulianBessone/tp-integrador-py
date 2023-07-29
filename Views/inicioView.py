import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Views.resultadosBusquedaView import ResultadosBusquedaView

class InicioView(tk.Frame):
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
        self.label_titulo = tk.Label(self, text="Food Travel App", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # Etiqueta para el input de búsqueda
        self.label_buscar = tk.Label(self, text="Buscar restaurantes:")
        self.label_buscar.pack(pady=10)

        # Input para que el usuario busque restaurantes
        self.input_buscar = tk.Entry(self)
        self.input_buscar.pack()

        # Botón para realizar la búsqueda
        self.boton_buscar = tk.Button(self, text="Buscar", command= lambda: self.controlador.buscar_restaurantes(self.input_buscar.get()))
        self.boton_buscar.pack(pady=5)

     
        # Separador para mejorar la apariencia
        tk.Frame(self, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)

        # Botones: Destinos, Reviews y Planificar Visita
        self.boton_destinos = tk.Button(self, text="Destinos", command= lambda: self.controlador.mostrar_destinos())
        self.boton_destinos.pack(pady=5)

        self.boton_reviews = tk.Button(self, text="Reviews", command= lambda: self.controlador.mostrar_reviews())
        self.boton_reviews.pack(pady=5)

        self.boton_planificar_visita = tk.Button(self, text="Planificar Visita", command=print('hola'))
        self.boton_planificar_visita.pack(pady=5)


        # Mostrar los destinos en una etiqueta
        self.label_destinos = tk.Label(self, text="Destinos:")
        self.label_destinos.pack()

        destinos_text = "\n".join([f"- {destino.nombre}" for destino in self.destinos])
        self.reviews_label = tk.Label(self, text=destinos_text, justify=tk.LEFT)
        self.reviews_label.pack()



