import tkinter as tk
from Models.reviews import Review

class ControladorReview:
    def __init__(self, app):
        self.app = app
        self.destinos = app.destinos

    def mostrar_cargar_review(self):
        self.app.cambiar_frame(self.app.vista_cargar_review)

    def seleccionar_destino_para_review(self, event):
        indice_seleccionado = self.app.vista_cargar_review.destino_listbox.curselection()
        indice_seleccionado =  indice_seleccionado[0]
        destino_seleccionado= self.destinos[indice_seleccionado]
        self.app.vista_cargar_review.destino_seleccionado = destino_seleccionado

        label_review = tk.Label(self.app.vista_cargar_review, text= f"Ingrese aquí su reseña del destino : {destino_seleccionado.nombre}")
        label_review.pack()
        #Creacion de entry para que el usuario ingrese su comentario
        #entry_review = tk.Entry(self.app.vista_cargar_review)
        #entry_review.pack()

        # Crear el Text para que el usuario ingrese el comentario con dimensiones grandes para agregar varias lineas
        text_review = tk.Text(self.app.vista_cargar_review, width=50, height=5)
        text_review.pack()

        # Almacenar el Text como un atributo del contenedor para acceder a él posteriormente
        self.app.vista_cargar_review.text_review = text_review

        # Almacenar el Entry como un atributo del contenedor para acceder a él posteriormente
        #self.app.vista_cargar_review.entry_review = entry_review

        # Crea el botón para guardar el comentario
        boton_guardar = tk.Button(self.app.vista_cargar_review, text="Guardar", command=lambda: self.guardar_comentario(text_review.get("1.0", tk.END)))
        boton_guardar.pack()
        # DESCOMENTAR PARA LUEGO PONER LA CALIFICACION (DE 1 A 5)
""" 
    def guardar_comentario(self, comentario):
        
        reviewNueva = Review((self.app.destinos.len() + 1), self.app.vista_cargar_review.destino_seleccionado.id, 1,)
        self.app.reviews.append()
        # Guarda el comentario en una base de datos
        print("Comentario guardado:")
        print(comentario) 



        print(indice)
        if indice:
            nombre_destino_seleccionado=self.listbox.get(indice[0])
            destino_seleccionado=next((destino for destino in self))  """
        
