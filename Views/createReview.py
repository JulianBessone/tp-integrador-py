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

        ## TODO - descomentar , conectarlo a la base de datos y hacer que funcione

        """ # # listbox de posibles destinos"""
        self.label_destino = tk.Label(self, text="Destino")
        self.label_destino.pack(pady=5)

        self.destino_listbox = tk.Listbox(self, width=80, height=20)

        for destino in self.destinos:
            self.destino_listbox.insert(tk.END, destino.nombre)

        self.destino_listbox.pack(pady=5)
        self.destino_listbox.bind(
            "<<ListboxSelect>>", self.controlador.seleccionar_destino_para_review
        )

        boton_volver = tk.Button(
            self,
            text="Volver",
            command=lambda: self.app.cambiar_frame(self.app.vista_inicio),
        )
        boton_volver.pack()

    def createReviewForm(self, destino):
        if hasattr(self.app.vista_cargar_review, "labelFormTitle"):
            self.app.vista_cargar_review.labelFormTitle.destroy()
            self.app.vista_cargar_review.text_review.destroy()
            self.app.vista_cargar_review.label_calificacion.destroy()
            self.app.vista_cargar_review.listbox_calificacion.destroy()
            self.app.vista_cargar_review.boton_cargar_review.destroy()
            self.app.vista_cargar_review.boton_volver.destroy()

        self.app.vista_cargar_review.labelFormTitle = tk.Label(
            self, text="Agrege su reseña del destino : " + destino.nombre + " :"
        )
        self.app.vista_cargar_review.labelFormTitle.pack(pady=10)
        self.app.vista_cargar_review.text_review = tk.Text(self, width=50, height=1)
        self.app.vista_cargar_review.text_review.pack(pady=5)
        self.app.vista_cargar_review.label_calificacion = tk.Label(
            self, text="Calificacion"
        )
        self.app.vista_cargar_review.label_calificacion.pack(pady=5)
        self.app.vista_cargar_review.listbox_calificacion = tk.Listbox(
            self, width=2, height=1
        )
        self.app.vista_cargar_review.listbox_calificacion.pack(pady=5)
        for calificacion in range(1, 6):
            self.app.vista_cargar_review.listbox_calificacion.insert(
                tk.END, calificacion
            )

        self.app.vista_cargar_review.listbox_calificacion.pack(pady=5)

        self.app.vista_cargar_review.boton_cargar_review = tk.Button(
            self,
            text="Cargar Review",
            command=lambda: self.controlador.cargar_review(
                {
                    "nameDestino": destino.nombre,
                    "idDestino": destino.id,
                    "text": self.app.vista_cargar_review.text_review.get("1.0", tk.END),
                    "calificacion": self.app.vista_cargar_review.listbox_calificacion.get(
                        tk.ACTIVE
                    ),
                }
            ),
        )

        self.app.vista_cargar_review.boton_cargar_review.pack()

        # volver atras
        self.app.vista_cargar_review.boton_volver = tk.Button(
            self,
            text="Volver",
            command=lambda: self.app.cambiar_frame(self.app.vista_inicio),
        )
        self.app.vista_cargar_review.boton_volver.pack()
