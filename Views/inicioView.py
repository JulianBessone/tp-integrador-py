import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Views.resultadosBusquedaView import ResultadosBusquedaView

class InicioView:
    def __init__(self, root, destinos):
        self.root = root
        self.destinos = destinos
        self.root.title("FoodTravels App")
        self.root.geometry("800x450")

        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para el texto "Food Travel App"
        self.label_titulo = tk.Label(self.root, text="Food Travel App", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # Etiqueta para el input de búsqueda
        self.label_buscar = tk.Label(self.root, text="Buscar restaurantes:")
        self.label_buscar.pack(pady=10)

        # Input para que el usuario busque restaurantes
        self.input_buscar = tk.Entry(self.root)
        self.input_buscar.pack()

        # Botón para realizar la búsqueda
        self.boton_buscar = tk.Button(self.root, text="Buscar", command=self.buscar_restaurantes)
        self.boton_buscar.pack(pady=5)

     
        # Separador para mejorar la apariencia
        tk.Frame(self.root, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)

        # Botones: Destinos, Reviews y Planificar Visita
        self.boton_destinos = tk.Button(self.root, text="Destinos", command=self.mostrar_destinos)
        self.boton_destinos.pack(pady=5)

        self.boton_reviews = tk.Button(self.root, text="Reviews", command=self.mostrar_reviews)
        self.boton_reviews.pack(pady=5)

        self.boton_planificar_visita = tk.Button(self.root, text="Planificar Visita", command=self.planificar_visita)
        self.boton_planificar_visita.pack(pady=5)


        # Mostrar las reviews en una etiqueta
        self.label_destinos = tk.Label(self.root, text="Destinos:")
        self.label_destinos.pack()

        destinos_text = "\n".join([f"- {destino.nombre}" for destino in self.destinos])
        self.reviews_label = tk.Label(self.root, text=destinos_text, justify=tk.LEFT)
        self.reviews_label.pack()


    def buscar_restaurantes(self):
        # Aquí puedes agregar la lógica para buscar restaurantes
        # por el término ingresado en el input.
        # Obtiene el término de búsqueda del input
        termino_busqueda = self.input_buscar.get()

        # Aquí puedes agregar la lógica para realizar la búsqueda utilizando el término ingresado.
        # Por ejemplo, podrías buscar en la lista de destinos los que coincidan con el término.

        # Muestra un mensaje de alerta si el término de búsqueda está vacío.
        if not termino_busqueda:
            messagebox.showwarning("Advertencia", "Ingresa un término de búsqueda.")
            return
        self.vista = ResultadosBusquedaView(self.root, self.destinos, termino_busqueda)


    def mostrar_destinos(self):
        # Aquí puedes agregar la lógica para mostrar los destinos.
        pass

    def mostrar_reviews(self):
        # Aquí puedes agregar la lógica para mostrar las reviews.
        pass

    def planificar_visita(self):
        # Aquí puedes agregar la lógica para planificar una visita.
        pass