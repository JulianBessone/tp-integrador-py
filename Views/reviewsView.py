import tkinter as tk
import customtkinter as ctk


class ReviewsVista(tk.Frame):
    def __init__(self, app, reviewsController, reviews, destinos, usuarios):
        super().__init__(app)
        self.app = app
        self.reviews = reviews
        self.controlador = reviewsController
        self.destinos = destinos
        self.usuarios = usuarios

        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Reseñas")
        self.app.geometry("800x850")

        self.create_widgets()

    def create_widgets(self):
        self.label_titulo = tk.Label(self, text="Reviews", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # Lista para mostrar los resultados de la búsqueda
        self.reviews_listbox = tk.Listbox(self, width=80, height=20)

        for review in self.reviews:
            """Deberias pasar por parametro la lista de destinos y luego dentro
            de este for buscar el destino correspondienta a id_destino del review"""
            self.reviews_listbox.insert(tk.END, "Calificación", review.calificacion)

            self.reviews_listbox.insert(tk.END, review.comentario)

            for destino in self.destinos:
                if destino.id == review.id_destino:
                    self.reviews_listbox.insert(tk.END, destino.nombre)
            # self.reviews_listbox.insert(tk.END, review.comentario)
            for usuario in self.usuarios:
                if usuario.id == review.id_usuario:
                    self.reviews_listbox.insert(
                        tk.END, usuario.nombre, usuario.apellido
                    )

            self.reviews_listbox.insert(tk.END, "------------")

        self.reviews_listbox.pack(pady=5)

        self.create_review_button = tk.Button(
            self,
            text="Agregar nueva Reseña",
            command=lambda: self.controlador.mostrar_cargar_review(),
        )
        self.create_review_button.pack(pady=5, padx=5)
