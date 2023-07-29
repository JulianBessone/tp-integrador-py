import tkinter as tk


class VistaDestinos(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la lista de destinos.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        self.titulo = tk.Label(self, text="Lista de Destinos")
        self.titulo.pack(pady=10)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

        # Asocia el evento de doble clic a la función seleccionar_destino
        self.listbox.bind("<Double-Button-1>", self.seleccionar_destino)

        self.listbox.pack(pady=10)
        self.actualizar_destinos()

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = tk.Button(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.pack(pady=10)

    def actualizar_destinos(self):
        """
        Actualiza la lista de destinos con los destinos obtenidos del controlador.
        """
        destinos = self.controlador.obtener_destinos()
        self.listbox.delete(0, tk.END)
        for destino in destinos:
            self.listbox.insert(tk.END, destino.nombre)

    def obtener_destino_seleccionado(self):
        """
        Retorna el índice del destino seleccionado en la lista.
        """
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_destino(self, event):
        """
        Obtiene el índice del destinoS seleccionado y llama al controlador para
        mostrar la información del destino.
        """
        self.controlador.seleccionar_destino()
