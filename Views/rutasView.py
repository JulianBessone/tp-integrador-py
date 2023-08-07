from tkinter import Frame, Label, Grid, N, S, E, W
import tkinter as tk
from datetime import datetime


class VistaRutas(tk.Frame):
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
        self.app.resizable(1, 1)

        self.create_widgets()


    def create_widgets(self):                

        self.titulo = tk.Label(self, text="Planifica tu visita", font=("Arial", 20))
        self.titulo.place(x=200,y=20)

        self.titulo = tk.Label(self, text="Busca por tipo de comida \n o actividad", font=("Arial", 14))
        self.titulo.place(x=10, y=90, anchor=tk.W)

        # Agregar un cuadro de texto para el buscador
        self.buscador_entrada = tk.Entry(self, width=40)
        self.buscador_entrada.place(x=10, y=120)

        # Asociar el evento de escritura al buscador
        self.buscador_entrada.bind("<KeyRelease>", self.filtrar_destinos)

        #listabox de destinos
        self.listbox_destinos = tk.Listbox(self, width=35, font=("Arial", 10))
        self.listbox_destinos.place(x=10, y=150)

        for destino in self.destinos:
            self.listbox_destinos.insert(tk.END, destino.nombre)

        self.listbox_destinos.bind("<<ListboxSelect>>", self.controlador.mostrar_informacion_destino)
        self.listbox_destinos.place(x=10, y=150)  


        # Etiquetas para mostrar los ingredientes y el tipo de cocina del destino seleccionado
        self.destino_label = tk.Label(self, text="", font=("Arial", 12))
        self.destino_label.place(x=300, y=150)

        self.tipo_cocina_label = tk.Label(self, text="", font=("Arial", 10))
        self.tipo_cocina_label.place(x=300, y=190)

        self.actividades_label = tk.Label(self, text="", font=("Arial", 10))
        self.actividades_label.place(x=300, y=220)


        # Crea el botón "Agregar a mi ruta" 
        # y el metodo agregar a ruta muestra una nueva ventana y le
        # paso el objeto seleccionado que viene de mostrar informacion en el controlador
        self.boton_agregar_ruta = tk.Button(
            self, 
            text="Agregar destino y ver rutas", 
            command=lambda: self.controlador.agregar_a_ruta(self.destino_seleccionado)
        )

        self.boton_agregar_ruta.place(x=300, y=300)



        # Crea el botón "Ir a Inicio" y lo agrega al contenedor
        self.boton_inicio = tk.Button(
             self, text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.place(x=400,y=420)



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






