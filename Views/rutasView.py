from tkinter import Frame, Label, Grid, N, S, E, W
import tkinter as tk
import customtkinter as ctk
from datetime import datetime
from PIL import Image, ImageTk


class VistaRutas(ctk.CTkFrame):
    def __init__(self, app, controladorRutas, destinos, actividades, rutas):
        super().__init__(app)
        self.app = app
        self.controlador = controladorRutas
        self.destinos = destinos
        self.actividades = actividades
        self.rutas = rutas
        self.destino_seleccionado = {} #es un objeto

        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Destinos")
        self.app.geometry("885x620")
        self.configure(fg_color='#F39116')
        #self.app.resizable(1, 1)

        self.create_widgets()


    def create_widgets(self):                

        self.titulo = ctk.CTkLabel(self, text="Planifica tu visita", font=("Arial", 30, 'bold'))
        self.titulo.place(x=300,y=20)


        self.titulo = ctk.CTkLabel(self, text="Busca tu destino ingresando \n el tipo de comida que te gusta o actividad que te interesa \n y agregalo a tu ruta", font=("Arial", 16, 'bold'))
        self.titulo.place(x=210, y=60)

        self.titulo = ctk.CTkLabel(self, text="Ingresa Tipo de comida o Actividad", font=("Arial", 14, 'bold'))
        self.titulo.place(x=10, y=130)

        # Agregar un cuadro de texto para el buscador
        self.buscador_entrada = ctk.CTkEntry(self, width=250)
        self.buscador_entrada.place(x=10, y=160)
        self.buscador_entrada.configure(fg_color='#E8DFDA', text_color='#23272d')

        # Asociar el evento de escritura al buscador
        self.buscador_entrada.bind("<KeyRelease>", self.filtrar_destinos)

        #listabox de destinos
        self.listbox_destinos = tk.Listbox(self, width=35, height=15, bg="#E8DFDA", font=("Arial", 10))
        self.listbox_destinos.place(x=10, y=190)

        for destino in self.destinos:
            self.listbox_destinos.insert(tk.END, destino.nombre)

        self.listbox_destinos.bind("<<ListboxSelect>>", self.controlador.mostrar_informacion_destino)



        # Etiquetas para mostrar los ingredientes y el tipo de cocina del destino seleccionado
        self.destino_label = ctk.CTkLabel(self, text="Destino", font=("Arial", 20, 'bold'), text_color="#267166")
        self.destino_label.place(x=300, y=130)

        self.tipo_cocina_titulo = ctk.CTkLabel(self, text="Tipo de cocina: ", font=("Arial", 16, 'bold'))
        self.tipo_cocina_titulo.place(x=300, y=170)

        self.tipo_cocina_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.tipo_cocina_label.place(x=300, y=200)

        self.actividades_titulo = ctk.CTkLabel(self, text="Actividades Programadas", font=("Arial", 16, 'bold'))
        self.actividades_titulo.place(x=300, y=230)

        self.actividades_label = ctk.CTkLabel(self, text="", font=("Arial", 14), justify="left")
        self.actividades_label.place(x=300, y=260)

        imagen = ctk.CTkImage(Image.open('assets/img/food-travel-app.jpg'), size=(250, 250))
        self.imagen_label = ctk.CTkLabel(self, image=imagen, text="")
        self.imagen_label.place(x=600, y=170)


        # Crea el botón "Agregar a mi ruta" 
        # y el metodo agregar a ruta muestra una nueva ventana y le
        # paso el objeto seleccionado que viene de mostrar informacion en el controlador
        self.boton_agregar_ruta = ctk.CTkButton(
            self, 
            text="Agregar destino y ver rutas", 
            command=lambda: self.controlador.agregar_a_ruta(self.destino_seleccionado)
        )

        self.boton_agregar_ruta.place(x=300, y=450)
        self.boton_agregar_ruta.configure(fg_color="#FF5722")



        # Crea el botón "Ir a Inicio" y lo agrega al contenedor
        self.boton_inicio = ctk.CTkButton(
             self, text="Volver", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.place(x=700,y=450)
        self.boton_inicio.configure(fg_color="#FF5722")



    def filtrar_destinos(self, event):
        """
        Filtra los destinos en el Listbox según el término de búsqueda ingresado en el cuadro de texto.
        """
        termino_busqueda = self.buscador_entrada.get().lower()
        destinos = self.controlador.destinos  # Usamos la lista de destinos del controlador

        # Filtrar destinos según el término de búsqueda
        destinos_filtrados = [destino for destino in destinos if
                              termino_busqueda in destino.tipo_cocina.lower() or
                              any(termino_busqueda in actividad.nombre.lower() for actividad in self.controlador.actividades if actividad.destino_id == destino.id)]

        # Actualizar el Listbox con los destinos filtrados
        self.listbox_destinos.delete(0, tk.END)
        for destino in destinos_filtrados:
            self.listbox_destinos.insert(tk.END, destino.nombre)

    def cargar_imagen(self, imagen_url):
        # Cargar la imagen desde la URL usando Pillow
        imgPath = f'assets/img/{imagen_url}'
        imagen = Image.open(imgPath)
        imagen = ctk.CTkImage(imagen, size=(250,250))
        self.imagen_label = ctk.CTkLabel(self, image=imagen, text="")
        self.imagen_label.place(x=600, y=170)

 




