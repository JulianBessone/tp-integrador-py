import tkinter as tk


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

        """ # # listbox de posibles destinos"""
        self.label_destino = tk.Label(self, text="Destino")
        self.label_destino.pack(pady=5)

        self.destino_listbox = tk.Listbox(self, width=80, height=20)

        for destino in self.destinos:
            self.destino_listbox.insert(tk.END, destino.nombre)

        self.destino_listbox.pack(pady=5)
        self.destino_listbox.bind("<<ListboxSelect>>", self.controlador.seleccionar_destino_para_review)
        

        for destino in self.destinos:
             if destino.nombre == self.destino_listbox.get(tk.ACTIVE):
                id_destino = destino.id
    
    def createReviewForm(self, destino):
        if hasattr(self.app.vista_cargar_review, 'labelFormTitle'):
            self.labelFormTitle.destroy()
            self.text_review.destroy()
           
        self.app.vista_cargar_review.labelFormTitle = tk.Label(self, text= f"Ingrese aquí su reseña del destino : {destino.nombre}")
        self.app.vista_cargar_review.labelFormTitle.pack()
        self.text_review = tk.Text(self.app.vista_cargar_review, width=50, height=5)
        self.text_review.pack()

        
     # # listbox de posibles destinos"""
        #self.label_review = tk.Label(self, text="Ingrese aquí su reseña de: ")
        #self.label_review.pack(pady=5)



        """# # listbox de posibles usuarios
""" 
"""         self.label_usuario = tk.Label(self, text="Usuario")

        self.label_usuario.pack(pady=5)

        self.usuario_listbox = tk.Listbox(self, width=80, height=20)

        for usuario in self.usuarios:
            self.usuario_listbox.insert(tk.END, usuario.nombre, usuario.apellido)

        self.usuario_listbox.pack(pady=5)

        for usuario in self.usuarios:
            if usuario.nombre == self.usuario_listbox.get(tk.ACTIVE):
                id_usuario = usuario.id """ """
 """ 