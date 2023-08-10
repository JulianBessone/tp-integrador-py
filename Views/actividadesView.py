import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime


class VistaActividades(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de las actividades del destino culinario.
        """
        super().__init__(master)
        self.master = master #le paso la aplicacion
        self.controlador = controlador  #le paso el controlador de actividad


    def mostrar_actividades_destino(self, destino):  
        """
        el parametro destino que recibe es la instancia del objeto
        Muestra la información del destino recibido como parámetro.
        """       


        #info = f"Destino: {destino.id} - {destino.nombre}"
        info = destino.nombre #propiedad nombre del objeto
        info_actividad = ""

        #CONFIGURACION DE LA GRILLA 2X2

        # Configurar las filas y columnas de la grilla
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) 
        #Crear un nuevo Frame dentro de la celda (fila 0, columna 1)
        sub_frame = tk.Frame(self)
        sub_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        # Configurar las filas y columnas de la nueva grilla (sub_frame) 9X1
 
        for i in range(9):
            sub_frame.grid_rowconfigure(i, weight=1)

        # Crear un nuevo Frame dentro de la celda (fila 1, columna 0) que ocupe las dos columnas
        sub_frame_1 = tk.Frame(self)
        sub_frame_1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configurar las columnas de la nueva grilla (sub_frame_1) 1X3
        for i in range(3):
            sub_frame_1.grid_columnconfigure(i, weight=1)
        #fin CONFIGURACION GRILLA          


        #IMAGEN - la imagen iria en fila 0 columna 0        
        # Obtener la URL de la imagen del destino desde el JSON
        imagen_url = destino.imagen  
        
        # Cargar la imagen desde la URL usando Pillow
        # la imagen iria en la columna 0 fila 0
        try:
            imgPath = f'assets/img/{imagen_url}'
            imagen = Image.open(imgPath)
            # Redimensionar la imagen si es necesario
            ancho=400
            alto=400
            imagen = imagen.resize((ancho, alto))

            imagen = ImageTk.PhotoImage(imagen)

            # Crear una etiqueta para mostrar la imagen
            self.imagen_label = tk.Label(self, image=imagen)
            self.imagen_label.image = imagen  # Mantener una referencia para evitar que la imagen se borre
            self.imagen_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        except Exception as e:
            # Si ocurre algún error al cargar la imagen, mostrar un mensaje
            print(f"Error al cargar la imagen: {e}")
            self.imagen_label = None    
        #fin IMAGEN    

        #INFORMACION DEL DESTINO A LA DERECHA 

        # Mostrar el texto del destino en la segunda celda de la nueva grilla (sub_frame)        
        self.destino_label = tk.Label(sub_frame, text=info, justify=tk.LEFT, font=("Arial", 20))
        self.destino_label.grid(row=0, column=0, sticky="nw")  # Alineación arriba a la izquierda

        # Mostrar el texto "Actividades programadas" en la segunda fila del sub_fram
        actividades_label = tk.Label(sub_frame, text="Actividades programadas", justify=tk.LEFT, font=("Arial", 16))
        actividades_label.grid(row=1, column=0, sticky="nsew")

        actividades = self.controlador.obtener_actividades_destino(destino.id)
        for actividad in actividades:
            # Convertir la fecha a un objeto datetime
            fecha_hora_obj = datetime.strptime(actividad.hora_inicio, "%Y-%m-%dT%H:%M:%S")
            # Formatear la fecha en formato dd/mm/aaaa
            fecha = fecha_hora_obj.strftime("%d/%m/%Y")
            # Formatear la hora en formato hh:mm
            hora = fecha_hora_obj.strftime("%H:%M")            
            info_actividad = info_actividad + f"{fecha}\n{actividad.nombre} - Inicia a las {hora}\n"
      
        self.destino_actividades_label = tk.Label(sub_frame, text=info_actividad)
        self.destino_actividades_label.grid(row=2, column=0, sticky="nw")  # Alineación arriba a la izquierda

    
        # #Agregar etiquetas con números en cada celda de la grilla -CONTROL GRILLA
        # for i in range(9):
        #     for j in range(3):
        #         numero = i * 3 + j
        #         etiqueta = tk.Label(sub_frame, text=str(numero))
        #         etiqueta.grid(row=i, column=j)



        # Mostrar el botón "Volver" en la segunda fila (segunda fila, segunda columna)

        # Mostrar los tres botones adicionales en la tercera fila (tercera fila, todas las columnas)
        # boton_1 = tk.Button(
        #     sub_frame_1,
        #     text="Ver Evento",
        #     command=self.funcion_boton_1,
        #     width=5,
        #     height=2,
        #     font=("Arial", 10),
        # )
        # boton_1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # boton_2 = tk.Button(
        #     sub_frame_1,
        #     text="Ver Reviews",
        #     command=self.funcion_boton_2,
        #     width=5,
        #     height=2,
        #     font=("Arial", 10),
        # )
        #boton_2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        boton_regresar = tk.Button(
            sub_frame_1,
            text="Volver",
            command=self.controlador.regresar_destinos,
            # width=5,
            # height=2,
            font=("Arial", 10, "bold"),
            # bg="blue",
            # fg="white",
        )
        boton_regresar.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")


        # Configurar las columnas del sub_frame para que tengan el mismo peso
        sub_frame.grid_columnconfigure(0, weight=1)
        sub_frame.grid_columnconfigure(1, weight=1)
        sub_frame.grid_columnconfigure(2, weight=1)



    def funcion_boton_1(self):
        # Código para el botón 1
        pass

    def funcion_boton_2(self):
        # Código para el botón 2
        pass

    def funcion_boton_3(self):
        # Código para el botón 3
        pass        