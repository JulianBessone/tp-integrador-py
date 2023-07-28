import tkinter as tk

class ReviewsVista(tk.Frame):
    def __init__(self, app, controlador, reviews):
        super().__init__(app)
        self.app = app
        self.reviews = reviews
        self.controlador = controlador
        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Reseñas")
        self.app.geometry("800x450")

        self.create_widgets()
    
    def create_widgets(self):

        self.label_titulo = tk.Label(self, text="Reviews", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # Lista para mostrar los resultados de la búsqueda
        self.reviews_listbox = tk.Listbox(self, width=80, height=20)

        for review in self.reviews:
            """Deberias pasar por parametro la lista de destinos y luego dentro de este for buscar el destino correspondienta a id_destino del review"""
            self.reviews_listbox.insert(tk.END, review.comentario)

        self.reviews_listbox.pack(pady=5)