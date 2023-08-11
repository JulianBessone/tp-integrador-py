import tkinter as tk
import customtkinter as ctk
from Views.inicioView import FrameDestino


class ResultadosBusquedaView(ctk.CTkFrame):
    def __init__(self, app, destinos, ubicaciones,termino_busqueda=""):
        super().__init__(app)
        self.app = app
        self.destinos = destinos
        self.ubicaciones = ubicaciones
        self.termino_busqueda = termino_busqueda
        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Resultados de búsqueda")
        self.app.geometry("800x450")
        self.configure(fg_color = '#F39116')

        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para el texto "Resultados de búsqueda"
        self.label_titulo = ctk.CTkLabel(
            self, text="Resultados de búsqueda", font=("Arial", 20)
        )
        self.label_titulo.pack(pady=10)

        # Lista para mostrar los resultados de la búsqueda
        self.resultados_listbox = tk.Listbox(self, width=80, height=20)

        # Agregar los resultados de la búsqueda a la lista
        resultados_encontrados = [
            destino
            for destino in self.destinos
            if self.termino_busqueda.lower() in destino.nombre.lower()
        ]
        self.frame_destinos = FrameDestino(self, resultados_encontrados, self.ubicaciones)
        self.frame_destinos.configure(width=855, height=395, fg_color='#F39116')
        self.frame_destinos.place(x=5, y=210)
    

        # Botón para volver a la vista anterior (InicioView)
        self.boton_volver = ctk.CTkButton(
            self,
            text="Volver a Inicio",
            width=150,  # Ajustar el ancho del botón
            height=30,  # Ajustar la altura del botón
            command=lambda:self.volver_al_inicio()
        )
        self.boton_volver.configure(fg_color='#FF5722')

        self.boton_volver.place(x=370, y=120)

    def actualizar_resultados(self, termino_busqueda):
        self.termino_busqueda = termino_busqueda
        self.frame_destinos.destroy() # Limpiar la lista actual
        resultados_encontrados = [
            destino
            for destino in self.destinos
            if self.termino_busqueda.lower() in destino.nombre.lower()
        ]
        self.frame_destinos = FrameDestino(self, resultados_encontrados, self.ubicaciones)
        self.frame_destinos.configure(width=855, height=395, fg_color='#F39116')
        self.frame_destinos.place(x=5, y=210)

    # def volver_a_inicio(self):
    #     # Destruye la ventana actual (ResultadosBusquedaView)
    #     # y muestra la vista anterior (InicioView)
    #     self.destroy()

    def volver_al_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
