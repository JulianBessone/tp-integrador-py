import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

# from tkinter import ttk
# from tkinter import messagebox
# from Views.resultadosBusquedaView import ResultadosBusquedaView


class InicioView(ctk.CTkFrame):
    def __init__(self, app, controladorInicio, destinos):
        super().__init__(app)
        self.app = app
        self.controlador = controladorInicio
        self.destinos = destinos
        self.app.geometry("1080x720")
        self.configure(fg_color='#F39116')


        # Colocar aquí el código para crear los widgets en este frame
        # Por ejemplo:
        self.create_widgets()

    def create_widgets(self):

        self.linea_separadora_ah = ctk.CTkLabel(self, text='', font=('Arial', 1, 'bold'), width=1000, height=0.5)
        self.linea_separadora_ah.configure(fg_color='#D13200')
        self.linea_separadora_ah.place(x=0, y=120)

        #Img:
        # rutaIMG = 'assets/img/background.jpg'
        # imagen_pil = Image.open(rutaIMG)
        # self.imagen = ImageTk.PhotoImage(imagen_pil)
        # etiqueta_imagen = tk.Label(self, image=self.imagen)
        # etiqueta_imagen.config(width=240, height=300)
        # etiqueta_imagen.place(x=10, y=280)

        # Etiqueta para el texto "Food Travel App"
        self.label_titulo = ctk.CTkLabel(self, text="Food Travel App", font=("Helvetica", 40, 'bold'))
        self.label_titulo.place(x=300, y=10)

        # Etiqueta para el input de búsqueda
        # self.label_buscar = ctk.CTkLabel(self, text="Buscar restaurantes:")
        # self.label_buscar.place(x=10, y=80)

        # Input para que el usuario busque restaurantes
        self.input_buscar = ctk.CTkEntry(self, width=550)
        self.input_buscar.configure(fg_color='#E8DFDA')
        self.input_buscar.place(x=9, y=80)

        # Botón para realizar la búsqueda
        self.boton_buscar = ctk.CTkButton(
    self,
    text="Buscar destino",
    width=150,  # Ajustar el ancho del botón
    height=30,  # Ajustar la altura del botón
    command=lambda: self.controlador.buscar_restaurantes(
        self.input_buscar.get()
            ),
        )
        self.boton_buscar.configure(fg_color='#FF5722')

        self.boton_buscar.place(x=570, y=80)
        #self.boton_buscar.pack(pady=5)


        # Botones: Destinos, Reviews y Planificar Visita


        self.boton_destinos = ctk.CTkButton(
            self,
            text="Destinos",
            width=200,
            height=40,
            command=lambda: self.controlador.mostrar_destinos())#Falta el controlador
        self.boton_destinos.configure(fg_color='#FF5722')
        self.boton_destinos.place(x=40, y=140) 
        #self.boton_destinos.pack(pady=5)

        self.boton_reviews = ctk.CTkButton(
            self,
            text="Reviews",
            width=200,
            height=40,
            command=lambda: self.controlador.mostrar_reviews()
        )
        self.boton_reviews.configure(fg_color='#FF5722')

        self.boton_reviews.place(x=340, y=140) 
        #self.boton_reviews.pack(pady=5)


        self.boton_planificar_visita = ctk.CTkButton(self,
        text="Planificar Visita",
        width=200,
        height=40,
        command= lambda: self.controlador.mostrar_rutas())
        self.boton_planificar_visita.configure(fg_color='#FF5722')
        self.boton_planificar_visita.place(x=640, y=140)
        #self.boton_planificar_visita.pack(pady=5)

        # Mostrar los destinos en una etiqueta
        self.label_destinos = ctk.CTkLabel(self, text="Destinos:")
        self.label_destinos.configure(fg_color='red')
        self.label_destinos.place(x=300, y=220)
        #self.label_destinos.pack()

        destinos_text = "\n".join([f"- {destino.nombre}" for destino in self.destinos])
        self.reviews_label = ctk.CTkLabel(self, text=destinos_text, justify=tk.LEFT)
        self.reviews_label.place(x=300, y=250)
        #self.reviews_label.pack()
