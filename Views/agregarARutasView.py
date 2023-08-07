from tkinter import Frame, Label, Grid, N, S, E, W
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class AgregarARutasView(tk.Frame):
    def __init__(self, app, controladorRutas, destinos, rutas):
        super().__init__(app)
        self.app = app
        self.controlador = controladorRutas
        self.destinos = destinos
        self.rutas = rutas
        self.ruta_seleccionada = {}

 


        """AQUI CAMBIO EL TAMAÑO Y EL TITULO DE LA VENTANA"""
        self.app.title("FoodTravels App - Agrega el destino a tu ruta")
        self.app.geometry("885x620")
        self.app.resizable(1, 1)

        self.create_widgets()


    def create_widgets(self):

        self.titulo = tk.Label(self, text="titulo", font=("Arial", 20))
        self.titulo.place(x=200,y=20)

        self.rutas_label = tk.Label(self, text="Selecciona la ruta", font=("Arial", 14))
        self.rutas_label.place(x=10,y=70)

        #muestro la lista de las rutas
        self.rutas_listbox = tk.Listbox(self, width=40, height=16)

        self.cargar_rutas()

        # for ruta in self.rutas:
        #     """Deberias pasar por parametro la lista de destinos y luego dentro de este for buscar el destino correspondienta a id_destino del review"""
        #     self.rutas_listbox.insert(tk.END, ruta.nombre)

        # self.rutas_listbox.place(x=10, y=100)
        self.rutas_listbox.bind('<<ListboxSelect>>', self.mostrar_destinos_ruta)

        # Crea el botón "Guardar" y lo agrega al contenedor
        self.boton_agregar_destino = tk.Button(
            self, 
            text="Agregar Destino a la \n ruta seleccionada", 
            command=lambda: self.controlador.agregar_destino(self.ruta_seleccionada)
        )

        self.boton_agregar_destino.place(x=260, y=200)  

        # self.destinos_text = ScrolledText(self)
        # self.destinos_text.place(x=220, y=100)
        self.destinos_ruta_listbox = tk.Listbox(self, width=60, height=16)
        self.destinos_ruta_listbox.place(x=400, y=100)

        # Botón "Nueva Ruta"
        self.boton_nueva_ruta = tk.Button(
            self,
            text="Nueva Ruta",
            command=self.mostrar_ventana_nueva_ruta
        )
        self.boton_nueva_ruta.place(x=20, y=370)

        # Boton volver y lo agrega al contenedor
        self.boton_volver = tk.Button(
             self, text="Volver", command=self.controlador.regresar_rutas
        )
        self.boton_volver.place(x=400,y=420)   

 
    def cargar_rutas(self):

        self.rutas_listbox.delete(0, tk.END)  # Limpiar la lista actual        

        for ruta in self.rutas:
            self.rutas_listbox.insert(tk.END, ruta.nombre)


        self.rutas_listbox.place(x=10, y=100)


    def mostrar_destinos_ruta(self, event):
        """
        Selecciona los destinos de la ruta seleccionada
        """         
        self.destinos_ruta_listbox.delete(0, tk.END)  # Limpiar la lista actual

        indice_seleccionado = self.app.vista_agregar_a_ruta.rutas_listbox.curselection()
        if indice_seleccionado:
            indice_seleccionado = indice_seleccionado[0] #el primer elemento de la tupla que devuelve curselection
            # de la lista tomo el valor del elemento seleccionado
            nombre_ruta_seleccionada = self.app.vista_agregar_a_ruta.rutas_listbox.get(indice_seleccionado)

            #con el nombre seleccionado del listbox, lo busco en la lista de objetos de las rutas
            for ruta in self.rutas:
                if ruta.nombre == nombre_ruta_seleccionada:
                    # print("ruta: ", ruta.id, " ", ruta.nombre)
                    ruta_seleccionada = ruta  #ruta_seleccionada tiene la instancia

            #se lo paso a esta vista
            self.app.vista_agregar_a_ruta.ruta_seleccionada = ruta_seleccionada 

            # Muestro el listado de los destinos de la ruta
            # la instancia de la ruta seleccionada esta en ruta_seleccionada, 
            # debo mostrar los destinos de esa ruta
            for destino in self.destinos:
                 for iddestino in ruta_seleccionada.destinos:
                     if destino.id == iddestino:
                        #print("destino: ", destino.id, " ", destino.nombre, " ", destino.tipo_cocina, " ", destino.popularidad)
                        nombre_destino = "Restaurante: " + destino.nombre
                        tipo_cocina = "Tipo de cocina: " + destino.tipo_cocina
                        popularidad = "Popularidad: " + str(destino.popularidad)
                        precios = "Precio mínimo: " + str(destino.precio_minimo) + " - Precio máximo: " + str(destino.precio_maximo)
                        self.destinos_ruta_listbox.insert(tk.END, nombre_destino)
                        self.destinos_ruta_listbox.insert(tk.END, tipo_cocina)
                        self.destinos_ruta_listbox.insert(tk.END, popularidad)
                        self.destinos_ruta_listbox.insert(tk.END, precios)
                        self.destinos_ruta_listbox.insert(tk.END, "------------")



    def mostrar_ventana_nueva_ruta(self):
        # Crear una ventana Toplevel para la nueva ruta
        ventana_nueva_ruta = tk.Toplevel(self)
        ventana_nueva_ruta.title("Nueva Ruta")
        #ventana_nueva_ruta.geometry("300x150")

        # Dimensiones de la ventana Toplevel
        ventana_ancho = 300
        ventana_alto = 150

        # Obtener las dimensiones de la pantalla
        pantalla_ancho = ventana_nueva_ruta.winfo_screenwidth()
        pantalla_alto = ventana_nueva_ruta.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (pantalla_ancho - ventana_ancho) // 2
        y = (pantalla_alto - ventana_alto) // 2

        # Establecer la geometría de la ventana
        ventana_nueva_ruta.geometry(f"{ventana_ancho}x{ventana_alto}+{x}+{y}")


        # Etiqueta y cuadro de texto para ingresar el nombre de la ruta
        etiqueta_nombre_ruta = tk.Label(
            ventana_nueva_ruta,
            text="Nombre de la nueva ruta:"
        )
        etiqueta_nombre_ruta.pack(pady=10)
        
        entry_nombre_ruta = tk.Entry(ventana_nueva_ruta)
        entry_nombre_ruta.pack(pady=5)

        # Botón para agregar la nueva ruta
        boton_agregar = tk.Button(
            ventana_nueva_ruta,
            text="Agregar Ruta",
            command=lambda: self.agregar_nueva_ruta(entry_nombre_ruta.get(), ventana_nueva_ruta)
        )
        boton_agregar.pack(pady=10)

    def agregar_nueva_ruta(self, nombre_ruta, ventana_nueva_ruta):
        if nombre_ruta:
            #si se agrego un nombre de ruta
            #agrego la ruta a json,
            self.controlador.guardar_ruta(nombre_ruta)

            # Cierra la ventana emergente después de agregar la ruta
            self.cargar_rutas()
            ventana_nueva_ruta.destroy()





