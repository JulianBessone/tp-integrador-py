import tkinter as tk

class ResultadosBusquedaView:
    def __init__(self, root, destinos, termino_busqueda):
        self.root = root
        self.destinos = destinos
        self.termino_busqueda = termino_busqueda
        """AQUI DEBERIA PONER ALGO QUE VACIE EL CONTENIDO DEL ROOT"""
        self.root.title("FoodTravels App - Resultados de búsqueda")
        self.root.geometry("800x450")

        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para el texto "Resultados de búsqueda"
        self.label_titulo = tk.Label(self.root, text="Resultados de búsqueda", font=("Arial", 20))
        self.label_titulo.pack(pady=10)

        # Lista para mostrar los resultados de la búsqueda
        self.resultados_listbox = tk.Listbox(self.root, width=80, height=20)

        # Agregar los resultados de la búsqueda a la lista
        resultados_encontrados = [destino for destino in self.destinos if self.termino_busqueda.lower() in destino.nombre.lower()]
        for resultado in resultados_encontrados:
            self.resultados_listbox.insert(tk.END, resultado.nombre)

        self.resultados_listbox.pack(pady=5)

        # Botón para volver a la vista anterior (InicioView)
        self.boton_volver = tk.Button(self.root, text="Volver", command=self.volver_a_inicio)
        self.boton_volver.pack(pady=5)

    def volver_a_inicio(self):
        # Destruye la ventana actual (ResultadosBusquedaView) y muestra la vista anterior (InicioView)
        self.root.destroy()
