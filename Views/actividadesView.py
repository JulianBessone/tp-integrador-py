import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import datetime


class VistaActividades(ctk.CTkFrame):
    def __init__(self, app, controlador, destinos, actividades):
        """
        Crea la vista de las actividades del destino culinario.
        """
        super().__init__(app)
        self.app = app #le paso la aplicacion
        self.controlador = controlador  #le paso el controlador de actividad
        self.destinos = destinos
        self.actividades = actividades
        self.configure(fg_color='#F39116')

        self.create_widgets()


    def create_widgets(self):

        #CONFIGURACION DE LA GRILLA 2X2

        # Configurar las filas y columnas de la grilla
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) 
        #Crear un nuevo Frame dentro de la celda (fila 0, columna 1)
        self.sub_frame = ctk.CTkFrame(self)
        self.sub_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.sub_frame.configure(fg_color='#F39116') 
        # Configurar las filas y columnas de la nueva grilla (sub_frame) 9X1
 
        for i in range(9):
            self.sub_frame.grid_rowconfigure(i, weight=1)

        # Crear un nuevo Frame dentro de la celda (fila 1, columna 0) que ocupe las dos columnas
        self.sub_frame_1 = ctk.CTkFrame(self)
        self.sub_frame_1.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.sub_frame_1.configure(fg_color='#F39116')

        # Configurar las columnas de la nueva grilla (sub_frame_1) 1X3
        for i in range(3):
            self.sub_frame_1.grid_columnconfigure(i, weight=1)
        #fin CONFIGURACION GRILLA                  

        #MOSTRAR DESTINO SELECCIONADO
        self.destino_label = ctk.CTkLabel(self.sub_frame, text="", font=("Arial", 22, 'bold'), text_color="#267166")
        self.destino_label.place(x=100,y=20)

        self.actividades_label = ctk.CTkLabel(self.sub_frame, text="Actividades programadas", font=("Arial", 16, 'bold'))
        self.actividades_label.place(x=100,y=60)

        self.destino_actividades_label = ctk.CTkLabel(self.sub_frame, text="", justify="left")
        self.destino_actividades_label.place(x=100, y=100)

        boton_regresar = ctk.CTkButton(
            self.sub_frame_1,
            text="Volver",
            command=self.controlador.regresar_destinos,
            font=("Arial", 12, "bold"),
        )

        boton_regresar.place(x=650,y=100)
        boton_regresar.configure(fg_color="#FF5722")


    def mostrar_actividades_destino(self, destino):  
        """
        el parametro destino que recibe es la instancia del objeto
        Muestra la información del destino recibido como parámetro.
        """       
        info = destino.nombre #propiedad nombre del objeto
        info_actividad = ""

        # Obtener la URL de la imagen del destino desde el JSON
        imagen_url = destino.imagen  
        
        # Cargar la imagen desde la URL usando Pillow
        try:
            imgPath = f'assets/img/{imagen_url}'
            imagen = Image.open(imgPath)
            # Redimensionar la imagen si es necesario
            ancho=400
            alto=400
            imagen = imagen.resize((ancho, alto))
    
            imagen = ctk.CTkImage(imagen, size=(ancho, alto))

            # Crear una etiqueta para mostrar la imagen
            self.imagen_label = ctk.CTkLabel(self, image=imagen, text="")
            self.imagen_label.image = imagen  # Mantener una referencia para evitar que la imagen se borre
            self.imagen_label.place(x=20, y=20)

        except Exception as e:
            # Si ocurre algún error al cargar la imagen, mostrar un mensaje
            print(f"Error al cargar la imagen: {e}")
            self.imagen_label = None    
        #fin IMAGEN    

        #INFORMACION DEL DESTINO 
        # Titulo del restaurant escogido        
        self.destino_label.configure(text=info)


        actividades = self.controlador.obtener_actividades_destino(destino.id)
        for actividad in actividades:
            # Convertir la fecha a un objeto datetime
            fecha_hora_obj = datetime.strptime(actividad.hora_inicio, "%Y-%m-%dT%H:%M:%S")
            # Formatear la fecha en formato dd/mm/aaaa
            fecha = fecha_hora_obj.strftime("%d/%m/%Y")
            # Formatear la hora en formato hh:mm
            hora = fecha_hora_obj.strftime("%H:%M")            
            info_actividad = info_actividad + f"{fecha}\n{actividad.nombre} - Inicia a las {hora}\n\n"
      
        if info_actividad == "":
            info_actividad ='No hay actividades programadas'
        self.destino_actividades_label.configure(text=f"{info_actividad}")


    