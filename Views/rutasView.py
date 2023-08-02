from tkinter import Frame, Label, Grid, N, S, E, W
import tkinter as tk
from datetime import datetime


class VistaRutas(tk.Frame):
    def __init__(self, app, controladorRutas):
        """
        Crea la vista de la lista de destinos.
        """
        super().__init__(app)
        self.app = app
        self.controlador = controladorRutas #controladorRutas

        # Establecer el color de fondo para el Frame
        #self.configure(background=self.fondo)


        # Agregar el título con la fuente Arial de tamaño 20
        #self.titulo = tk.Label(self, text="Planifica tu visita", font=("Arial", 20), bg=self.fondo, fg=self.color_naranja)
        self.titulo = tk.Label(self, text="Planifica tu visita", font=("Arial", 20))
        self.titulo.place(x=200,y=20)

        #self.titulo = tk.Label(self, text="Ingresa el tipo de comida \n o la actividad que te interese", font=("Arial", 14), bg=self.fondo, fg=self.color_verde)
        self.titulo = tk.Label(self, text="Busca por tipo de comida \n o actividad", font=("Arial", 14))
        self.titulo.place(x=10, y=90, anchor=tk.W)

        # Agregar un cuadro de texto para el buscador
        self.buscador_entry = tk.Entry(self, width=40)
        self.buscador_entry.place(x=10, y=120)

        # Asociar el evento de escritura al buscador
        self.buscador_entry.bind("<KeyRelease>", self.filtrar_destinos)

        #self.listbox = tk.Listbox(self, width=35, fg="#595959", font=("Arial", 10))
        self.listbox = tk.Listbox(self, width=35, font=("Arial", 10))
        self.listbox.place(x=10, y=150)

        # Asocia el evento de selección del Listbox a la función mostrar_informacion_destino
        self.listbox.bind("<<ListboxSelect>>", self.mostrar_informacion_destino)

        self.listbox.place(x=10, y=150)  
        self.actualizar_destinos()

        # Etiquetas para mostrar los ingredientes y el tipo de cocina del destino seleccionado
        self.destino_label = tk.Label(self, text="", font=("Arial", 12))
        self.destino_label.place(x=300, y=150)

        self.tipo_cocina_label = tk.Label(self, text="", font=("Arial", 10))
        self.tipo_cocina_label.place(x=300, y=190)

        self.actividades_label = tk.Label(self, text="", font=("Arial", 10))
        self.actividades_label.place(x=300, y=220)


        # #widgests de la tercera columna

        # # Título "Tu ruta actual"
        # self.titulo_ruta_actual = tk.Label(self, text="Tus rutas",font=("Arial", 14))
        # self.titulo_ruta_actual.place(x=700, y=90)

        # # Listbox para mostrar el listado de rutas con nombre y destinos
        # self.listbox_rutas = tk.Listbox(self, width=30)

        # # Asocia el evento de selección del Listbox a la función mostrar_informacion_destino
        # self.listbox_rutas.bind("<<ListboxSelect>>", self.obtener_mis_rutas)
        # self.listbox_rutas.place(x=700, y=120)
        # # Aquí debes cargar el listado de rutas con su nombre y destinos en el listbox_rutas
        # self.obtener_mis_rutas()





        # # Botón "Nueva Ruta"
        # self.boton_nueva_ruta = tk.Button(
        #     self.frame_grilla, text="Nueva Ruta", command=self.crear_ventana_nueva_ruta
        # )
        # self.boton_nueva_ruta.grid(row=2, column=3, padx=5, pady=5, sticky='w')

        # Crea el botón "Agregar a mi ruta" y lo agrega al contenedor
        self.boton_agregar_ruta = tk.Button(
            self, text="Agregar a mi ruta", command=self.agregar_a_ruta
        )
        self.boton_agregar_ruta.place(x=300, y=300)

        # Crea el botón "Ir a Inicio" y lo agrega al contenedor
        self.boton_inicio = tk.Button(
             self, text="Ir a Inicio", command=self.controlador.regresar_inicio
        )
        self.boton_inicio.place(x=400,y=420)

   

    def crear_ventana_nueva_ruta(self):
        # Crear la ventana Toplevel
        ventana_nueva_ruta = tk.Toplevel(self)
        ventana_nueva_ruta.title("Nueva Ruta")

        # # Etiqueta y cuadro de texto para ingresar el nombre de la ruta
        # etiqueta_nombre_ruta = tk.Label(ventana_nueva_ruta, text="Nombre de la ruta:")
        # etiqueta_nombre_ruta.pack(pady=5)
        # entry_nombre_ruta = tk.Entry(ventana_nueva_ruta)
        # entry_nombre_ruta.pack(pady=5)

        # # Botón para agregar la nueva ruta
        # boton_agregar = tk.Button(
        #     ventana_nueva_ruta, text="Agregar Ruta",
        #     command=lambda: self.agregar_nueva_ruta(entry_nombre_ruta.get(), ventana_nueva_ruta)
        # )
        # boton_agregar.pack(pady=5)

    def actualizar_destinos(self):
        """
        Actualiza la lista de destinos (listbox) 
        con los destinos obtenidos del controlador.
        """
        destinos = self.controlador.obtener_destinos()
        self.listbox.delete(0, tk.END)
        for destino in destinos:
            self.listbox.insert(tk.END, destino.nombre)


    def obtener_destino_seleccionado(self):
        """
        Retorna el destino_id del destino seleccionado en la lista.
        """
        indice = self.listbox.curselection()
        print(indice)
        if indice:
            nombre_destino_seleccionado = self.listbox.get(indice[0])
            destino_seleccionado = next((destino for destino in self.controlador.obtener_destinos() if destino.nombre == nombre_destino_seleccionado), None)
            if destino_seleccionado:
                return destino_seleccionado.id
        return None   


    def filtrar_destinos(self, event):
        """
        Filtra los destinos en el Listbox según el término de búsqueda ingresado en el cuadro de texto.
        """
        termino_busqueda = self.buscador_entry.get().lower()
        destinos = self.controlador.destinos  # Usamos la lista de destinos del controlador

        # Filtrar destinos según el término de búsqueda
        destinos_filtrados = [destino for destino in destinos if
                              termino_busqueda in destino.tipo_cocina.lower() or
                              any(termino_busqueda in actividad.nombre.lower() for actividad in self.controlador.actividades if actividad.destino_id == destino.id)]

        # Actualizar el Listbox con los destinos filtrados
        self.listbox.delete(0, tk.END)
        for destino in destinos_filtrados:
            self.listbox.insert(tk.END, destino.nombre)


    def mostrar_informacion_destino(self, event):
        """
        Muestra los ingredientes y el tipo de cocina del destino 
        seleccionado en las etiquetas.
        """
        indice = self.obtener_destino_seleccionado()
        if indice is not None:
            destino_seleccionado = self.controlador.obtener_destinos()[indice -1]
#            ingredientes = ", ".join(destino_seleccionado.ingredientes)
            tipo_cocina = destino_seleccionado.tipo_cocina
            nombre = destino_seleccionado.nombre

            # Obtener actividades del destino seleccionado
            actividades_destino = [actividad.nombre for actividad in self.controlador.actividades if actividad.destino_id == destino_seleccionado.id]

            self.destino_label.config(text=f"{nombre}")
            #self.ingredientes_label.config(text=f"Ingredientes: {ingredientes}")
            self.tipo_cocina_label.config(text=f"Tipo de cocina: {tipo_cocina}")

            # Actualizar etiqueta con las actividades del destino
            self.actividades_label.config(text=f"Actividades: {', '.join(actividades_destino)}")
        else:
            # Si no se ha seleccionado ningún destino, borrar el 
            # contenido de las etiquetas
            self.destino_label.config(text="")
            self.tipo_cocina_label.config(text="")
            self.actividades_label.config(text="")




    def agregar_nueva_ruta(self, nombre_ruta, ventana_nueva_ruta):
        """
        Agrega una nueva ruta con el nombre ingresado a la lista de rutas.
        Cierra la ventana Toplevel después de agregar la ruta.
        """
        if nombre_ruta:

            # Llamar al método agregar_ruta del controlador
            rutas = self.controlador.agregar_ruta(nombre_ruta, ventana_nueva_ruta)

            # Actualizar el Listbox con las rutas
            self.obtener_mis_rutas()

            # Cerrar la ventana Toplevel
            #ventana_nueva_ruta.destroy()
            #
            #ventana_nueva_ruta.withdraw()
             
    def ver_mis_rutas(self):
        """
        Función para ver las rutas de visita del usuario.
        Aquí puedes implementar la lógica para mostrar las rutas de visita del usuario.
        """
        # Implementa la lógica para mostrar las rutas de visita del usuario
        print("Ver mis rutas") 
  

    def obtener_mis_rutas(self):
        # traigo las rutas del controaldor
        rutas = self.controlador.obtener_rutas()

        self.listbox_rutas.delete(0, tk.END)

        # Agregar los nombres al Listbox
        for ruta in rutas:
            self.listbox_rutas.insert(tk.END, ruta.nombre)
            print(ruta.nombre)



    def agregar_a_ruta(self):
        indice = self.obtener_destino_seleccionado()
        if indice is not None:
            destino_seleccionado = self.controlador.obtener_destinos()[indice]
            nombre_destino = destino_seleccionado.nombre

            # Crear la ventana Toplevel
            ventana_destino_seleccionado = tk.Toplevel(self)
            ventana_destino_seleccionado.title("Agrega tu destino a la ruta")

            # Dimensiones de la ventana TopLevel
            ventana_ancho = 400
            ventana_alto = 400

            # Obtener las dimensiones de la pantalla
            pantalla_ancho = ventana_destino_seleccionado.winfo_screenwidth()
            pantalla_alto = ventana_destino_seleccionado.winfo_screenheight()

            # Calcular las coordenadas para centrar la ventana
            x = (pantalla_ancho - ventana_ancho) // 2
            y = (pantalla_alto - ventana_alto) // 2

            # Establecer la geometría de la ventana
            ventana_destino_seleccionado.geometry(f"{ventana_ancho}x{ventana_alto}+{x}+{y}")


            # Etiqueta para mostrar el destino seleccionado
            etiqueta_destino_seleccionado = tk.Label(ventana_destino_seleccionado, text=f"{nombre_destino}", font=("Arial", 16))
            etiqueta_destino_seleccionado.pack(padx=10, pady=10)

            # Título para el Listbox de selección de rutas
            titulo_listbox_rutas = tk.Label(ventana_destino_seleccionado, text="Seleccione la ruta", font=("Arial", 14))
            titulo_listbox_rutas.pack()

                            
            # Listbox para mostrar el listado de rutas desde el archivo "rutas.json"
            listbox_rutas = tk.Listbox(ventana_destino_seleccionado, width=40, height=10, font=("Arial", 12))
            listbox_rutas.pack(padx=10, pady=10)
 

            rutas = self.controlador.obtener_rutas()
            listbox_rutas.delete(0, tk.END)

            # Agregar los nombres al Listbox
            for ruta in rutas:
                listbox_rutas.insert(tk.END, ruta.nombre)

            # Botón para agregar el destino a la ruta seleccionada
            boton_agregar_destino = tk.Button(ventana_destino_seleccionado, text="Agregar destino a ruta", command=self.agregar_destino_a_ruta)
            boton_agregar_destino.pack(pady=10)                




            # # Listbox para mostrar los destinos de la ruta seleccionada
            # listbox_destinos_ruta = tk.Listbox(ventana_destino_seleccionado, width=40, height=10, font=("Arial", 12))
            # listbox_destinos_ruta.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        def mostrar_destinos_ruta(event):
            # Obtener el índice de la ruta seleccionada en listbox_rutas_json
            indice_ruta_seleccionada = listbox_rutas.curselection()
            if indice_ruta_seleccionada:
                indice_ruta = indice_ruta_seleccionada[0]

                # Obtener el nombre de la ruta seleccionada
                nombre_ruta_seleccionada = listbox_rutas.get(indice_ruta)

                # Buscar la ruta seleccionada en el archivo "rutas.json"
                with open("Data/rutas.json", "r") as archivo:
                    data = json.load(archivo)
                    for ruta in data["rutas"]:
                        if ruta["nombre"] == nombre_ruta_seleccionada:
                            # Limpiar el Listbox antes de agregar los destinos
                            listbox_destinos_ruta.delete(0, tk.END)

                            # Agregar los destinos de la ruta al Listbox
                            for destino in ruta["destinos"]:
                                listbox_destinos_ruta.insert(tk.END, destino)

                # Asociar el evento de selección del Listbox listbox_rutas_json a la función mostrar_destinos_ruta
                listbox_rutas.bind("<<ListboxSelect>>", mostrar_destinos_ruta) 

                # Botón para cerrar la ventana Toplevel
                boton_cerrar = tk.Button(ventana_destino_seleccionado, text="Cerrar", command=ventana_destino_seleccionado.destroy)
                boton_cerrar.pack(pady=10) 


        def agregar_destino_a_ruta(self):
            # Lógica para agregar el destino seleccionado a la ruta seleccionada
            pass

