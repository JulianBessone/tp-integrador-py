
#Importamos tkinter con el alias tk:
import tkinter as tk
import customtkinter as ctk
from tkintermapview import TkinterMapView
""" #Impotamos Themes Tkinter:
from tkinter import ttk

#Importamos TkinterMapView(para el mapa):
from tkintermapview import TkinterMapView

#Importamos Image y ImageTk de la libreria PIL(para las imagenes):
from PIL import Image, ImageTk """
from PIL import Image, ImageTk



#Clase principal de la vista:
class DestinosView(ctk.CTkFrame):

    #Método constructor:
    def __init__(self, app, controlador, destinos, ubicaciones):
        super().__init__(app)
        self.app = app
        self.controlador = controlador
        self.destinos = destinos
        self.ubicaciones = ubicaciones
        self.marcadores = ubicaciones
        self.destino_seleccionado = None

        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Destinos")
        self.app.geometry("885x620")
        self.app.resizable(1, 1)
        self.configure(fg_color='#F39116')

        self.create_widgets()
        

    def desvincular_evento_seleccion(self):
        self.destinos_listbox.unbind('<<ListboxSelect>>')

    def vincular_evento_seleccion(self):
        self.destinos_listbox.bind('<<ListboxSelect>>', self.controlador.seleccionar_destinos)
    
    def dibujar_destino_info(self):
        if(self.frameInfoDestino == None):
            self.frameInfoDestino = frame_container_info_destinos(self, self.destino_seleccionado)
            self.frameInfoDestino.place(x=12, y=540)
            self.frameInfoDestino.place_configure(width=245, height=70)
        else:
            self.frameInfoDestino.destroy()
            self.frameInfoDestino = frame_container_info_destinos(self, self.destino_seleccionado)
            self.frameInfoDestino.place(x=12, y=540)
            self.frameInfoDestino.place_configure(width=245, height=70)

    def create_widgets(self):

        self.destino_label_title = ctk.CTkLabel(self, text='Destinos:', font=('Helvetica', 25, 'bold'))
        self.destino_label_title.place(x=12, y=10)

        ##AQUI CREO LA LISTA DE DESTINOS
        self.destinos_listbox = tk.Listbox(self, width=40, height=16, border=3)

        for destino in self.destinos:
            """Deberias pasar por parametro la lista de destinos y luego dentro de este for buscar el destino correspondienta a id_destino del review"""
            self.destinos_listbox.insert(tk.END, destino.nombre)

        self.destinos_listbox.grid(row=0, column=0, padx=10, pady=(50, 10), sticky="n")
        self.destinos_listbox.bind('<<ListboxSelect>>', self.controlador.seleccionar_destinos)
        self.destinos_listbox.bind("<Double-Button-1>", self.seleccionar_destino)
        # self.destinos_listbox.bind('<<ListboxSelect>>', self.controlador.seleccionar_destinos_ubi)

        buttom_volver = ctk.CTkButton(self, text='Volver', command=lambda:self.controlador.mostrar_inicio())
        buttom_volver.configure(width=40, height=5)
        buttom_volver.place(x=180 ,y=585)

        ##MAPA VISTA
        self.mapa = TkinterMapView(self, width=600, height=600, corner_radius=20)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(14)
        self.mapa.grid(row=0, column=1, padx=10, pady=10, sticky="nsew",rowspan=2)
        self.mapa.set_marker(-24.77616437851034, -65.41079411004006)

        for ubicacion in (self.marcadores):
            self.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, '')
        
        self.frameInfoDestino = None


        ##AGREGAR MARCADORES DE DESTINOS
    def agregar_marcador_mapa(self, latitud, longitud, texto):
        return self.mapa.set_marker(latitud, longitud, text=texto)

       



        # self.tituloDetalleDestino = ctk.CTkLabel(self, text='INFORMACIÓN DEL DESTINO', font=('Helvetica', 15, 'bold'))
        # self.tituloDetalleDestino.configure(width=30, height=3, pady=0)
        # self.tituloDetalleDestino.place(x=12, y=540)


        # self.textoDisponiblidad = ctk.CTkLabel(self, width=30, height=1, font=('Helvetica', 13, 'bold'))
        # if self.destino_seleccionado.disponibilidad == 1:
        #     self.textoDisponiblidad.configure(text='Disponibilidad: Abierto')
        # else:
        #     self.textoDisponiblidad.configure(text='Disponivilidad: Cerrado')
        # self.textoDisponiblidad.place(x=20, y=560)
        # self.textoPopularidad = ctk.CTkLabel(self, width=30, height=1, font=('Helvetica', 13, 'bold'))
        # self.textoPopularidad.configure(text=f'Popularidad: {self.destino_seleccionado.popularidad}')
        # self.textoPopularidad.place(x=20, y=580)
        

    def obtener_destino_seleccionado(self):
        """
        Retorna el índice del destino seleccionado en la lista.
        """
        indice = self.destinos_listbox.curselection()
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

class frame_container_info_destinos(ctk.CTkFrame):
    def __init__(self, app, destino):
        super().__init__(app)
        self.app = app
        self.destino = destino

        self.tituloDetalleDestino = ctk.CTkLabel(self, text='INFORMACIÓN DEL DESTINO', font=('Helvetica', 15, 'bold'))
        self.tituloDetalleDestino.configure(width=30, height=3, anchor='w', justify=tk.LEFT)
        self.tituloDetalleDestino.grid(row=0, column=0, padx=7,pady=(7, 10))


        self.textoDisponiblidad = ctk.CTkLabel(self, width=30, height=1, font=('Helvetica', 13, 'bold'))
        if self.destino.disponibilidad == 1:
            self.textoDisponiblidad.configure(text='Disponibilidad: Abierto')
        else:
            self.textoDisponiblidad.configure(text='Disponivilidad: Cerrado')
        self.textoDisponiblidad.grid(row=1, column=0, sticky='w', padx=(7, 0))
        self.textoPopularidad = ctk.CTkLabel(self, width=30, height=1, font=('Helvetica', 13, 'bold'))
        self.textoPopularidad.configure(text=f'Popularidad: {self.destino.popularidad}')
        self.textoPopularidad.grid(row=2, column=0, sticky='w', padx=(7, 0))
        self.buttom_volver = ctk.CTkButton(self, text='Volver', command=lambda:self.app.controlador.mostrar_inicio())
        self.buttom_volver.configure(width=40, height=5)
        self.buttom_volver.place(x=168 ,y=45)