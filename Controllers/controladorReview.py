import tkinter as tk
import customtkinter as ctk
from Models.reviews import Review

import tkinter as tk
from Models.reviews import Review


class ControladorReview:
    def __init__(self, app):
        self.app = app
        self.destinos = app.destinos

    def mostrar_cargar_review(self):
        self.app.cambiar_frame(self.app.vista_cargar_review)

    def seleccionar_destino_para_review(self, event):
        indice_seleccionado = (
            self.app.vista_cargar_review.destino_listbox.curselection()
        )
        indice_seleccionado = indice_seleccionado[0]
        destino_seleccionado = self.destinos[indice_seleccionado]
        self.app.vista_cargar_review.destino_seleccionado = destino_seleccionado

        self.app.vista_cargar_review.createReviewForm(destino_seleccionado)


    def cargar_review(self, review):
        if review["calificacion"] < 3:
            review["sentimiento"] = "Negativo"
        # si review es neutro
        elif review["calificacion"] == 3:
            review["sentimiento"] = "Neutro"
        else:
            review["sentimiento"] = "Positivo"
        reviewNueva = Review(
            Review.generate_id("data/reviews.json"),
            review["idDestino"],
            1,  # cambiar por el id del usuario
            review["calificacion"],
            review["text"],
            review["sentimiento"],
        )
        # guardo el json
        reviewNueva.add_to_json("data/reviews.json")
        # guardo la review en el contenedor
        self.app.reviews.append(reviewNueva)
        # # cambio a la vista de inicio
        self.app.cambiar_frame(self.app.vista_inicio)
    
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)


