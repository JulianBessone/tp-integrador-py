import tkinter as tk
import customtkinter as ctk


class CreateReview(tk.Frame):
    def __init__(self, app, controlador, reviews, destinos, usuarios):
        super().__init__(app)
        self.app = app
        self.reviews = reviews
        self.controlador = controlador
        self.destinos = destinos
        self.usuarios = usuarios

        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Reseñas")
        self.app.geometry("800x850")

        self.create_widgets()

    def create_widgets(self):
        self.label_titulo = tk.Label(self, text="Reviews", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        
