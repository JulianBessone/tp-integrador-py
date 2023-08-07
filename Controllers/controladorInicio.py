import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox


class ControladorInicio:
    def __init__(self, app):
        # Aqui el controlador recibe la app para poder
        # acceder a sus funciones p/cambiar la vista
        self.app = app

    def mostrar_destinos(self):
        self.app.cambiar_frame(self.app.vista_destinos)

    def mostrar_actividades(self):
        self.app.cambiar_frame(self.app.vista_actividades)

    def mostrar_reviews(self):
        self.app.cambiar_frame(self.app.vista_reviews)

    def mostrar_rutas(self):
        self.app.cambiar_frame(self.app.vista_rutas)

    def buscar_restaurantes(self, input_buscar):
        # Obtiene el término de búsqueda del input
        termino_busqueda = input_buscar

        # Muestra un mensaje de alerta si el término de búsqueda está vacío.
        if not termino_busqueda:
            messagebox.showwarning("Advertencia", "Ingresa un término de búsqueda.")
            return

        # Cambio la vista a la vista de resultados de busqueda
        self.app.cambiar_frame(self.app.vista_resultados_busqueda)
        # Actualizo los resultados en base a lo que ingrese el user
        self.app.vista_resultados_busqueda.actualizar_resultados(termino_busqueda)