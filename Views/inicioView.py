import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw


# from tkinter import ttk
# from tkinter import messagebox
# from Views.resultadosBusquedaView import ResultadosBusquedaView


class InicioView(ctk.CTkFrame):
    def __init__(self, app, controladorInicio, destinos, ubicaciones):
        super().__init__(app)
        self.app = app
        self.controlador = controladorInicio
        self.destinos = destinos
        self.ubicaciones = ubicaciones
        self.app.geometry("1080x720")
        self.configure(fg_color='#F39116')



        # Colocar aquí el código para crear los widgets en este frame
        # Por ejemplo:
        self.create_widgets()

    def create_widgets(self):

        self.destinos_title = ctk.CTkLabel(self, text='Nuestros destinos:')
        self.destinos_title.configure(font=('Helvetica', 15, 'bold'), text_color='#23272d')
        self.destinos_title.place(x=9, y=180)

        #Frame scroll destinos:
        self.frame_destinos = FrameDestino(self, self.destinos, self.ubicaciones)
        self.frame_destinos.configure(width=855, height=395, fg_color='#F39116')
        self.frame_destinos.place(x=5, y=210)

        self.linea_separadora_ah = ctk.CTkLabel(self, text='', font=('Arial', 1, 'bold'), width=1000, height=0.5)
        self.linea_separadora_ah.configure(fg_color='#D13200')
        self.linea_separadora_ah.place(x=0, y=120)

        #Img:
        # rutaIMG = 'assets/img/background.jpg'
        # imagen_pil = Image.open(rutaIMG)
        # self.imagen = ImageTk.PhotoImage(imagen_pil)
        # etiqueta_imagen = tk.Label(self, image=self.imagen)
        # etiqueta_imagen.config(width=240, height=300)
        # etiqueta_imagen.place(x=10, y=280)

        # Etiqueta para el texto "Food Travel App"
        self.label_titulo = ctk.CTkLabel(self, text="Food Travel App", font=("Helvetica", 40, 'bold'))
        self.label_titulo.place(x=300, y=10)

        # Etiqueta para el input de búsqueda
        # self.label_buscar = ctk.CTkLabel(self, text="Buscar restaurantes:")
        # self.label_buscar.place(x=10, y=80)

        # Input para que el usuario busque restaurantes
        self.input_buscar = ctk.CTkEntry(self, width=550)
        self.input_buscar.configure(fg_color='#E8DFDA', text_color='#23272d')
        self.input_buscar.place(x=9, y=80)

        # Botón para realizar la búsqueda
        self.boton_buscar = ctk.CTkButton(
            self,
            text="Buscar destino",
            width=150,  # Ajustar el ancho del botón
            height=30,  # Ajustar la altura del botón
            command=lambda: self.controlador.buscar_restaurantes(
                self.input_buscar.get()
                    ),
        )
        self.boton_buscar.configure(fg_color='#FF5722')

        self.boton_buscar.place(x=570, y=80)
        #self.boton_buscar.pack(pady=5)


        # Botones: Destinos, Reviews y Planificar Visita


        self.boton_destinos = ctk.CTkButton(
            self,
            text="Destinos",
            width=200,
            height=40,
            command=lambda: self.controlador.mostrar_destinos())#Falta el controlador
        self.boton_destinos.configure(fg_color='#FF5722')
        self.boton_destinos.place(x=40, y=140) 
        #self.boton_destinos.pack(pady=5)

        self.boton_reviews = ctk.CTkButton(
            self,
            text="Reviews",
            width=200,
            height=40,
            command=lambda: self.controlador.mostrar_reviews()
        )
        self.boton_reviews.configure(fg_color='#FF5722')

        self.boton_reviews.place(x=340, y=140) 
        #self.boton_reviews.pack(pady=5)


        self.boton_planificar_visita = ctk.CTkButton(self,
        text="Planificar Visita",
        width=200,
        height=40,
        command= lambda: self.controlador.mostrar_rutas())
        self.boton_planificar_visita.configure(fg_color='#FF5722')
        self.boton_planificar_visita.place(x=640, y=140)
        #self.boton_planificar_visita.pack(pady=5)

        # # Mostrar los destinos en una etiqueta
        # self.label_destinos = ctk.CTkLabel(self, text="Destinos:")
        # self.label_destinos.configure(fg_color='red')
        # self.label_destinos.place(x=300, y=220)
        # #self.label_destinos.pack()

        # destinos_text = "\n".join([f"- {destino.nombre}" for destino in self.destinos])
        # self.reviews_label = ctk.CTkLabel(self, text=f'{destinos_text}', justify=tk.LEFT)
        # self.reviews_label.place(x=300, y=250)
        #self.reviews_label.pack()


class FrameDestino(ctk.CTkScrollableFrame):
    def __init__(self, app, destinos, ubicaciones):
        super().__init__(app)
        self.destinos = destinos
        self.ubicaciones = ubicaciones
        acc = 0
        for destino in self.destinos:

            nombre = destino.nombre
            tipoComida = destino.tipo_cocina
            rangoPrecio = f'${destino.precio_minimo}-${destino.precio_maximo}'
            direccion = None
            img = destino.imagen
            for ubicacion in ubicaciones:
                if ubicacion.id == destino.id_ubicacion:
                    direccion = ubicacion.direccion
                break
            

            frame_card = FrameCard(self, nombre, tipoComida, rangoPrecio, direccion, img)
            frame_card.configure(width=659, height=300, fg_color='#E8DFDA', corner_radius=30)
            #frame_card.configure(fg_color='red')
            frame_card.grid(row=acc, column=0, pady=(0, 10))



            acc += 1
        # self.label_ej = ctk.CTkLabel(self, text='Hello world')

        # self.label_destinos = ctk.CTkLabel(self, text=f'{destinos_text}', justify=tk.LEFT)
        # self.label_destinos.grid(row=0, column=0)


class FrameCard(ctk.CTkFrame):
    
    def __init__(self, app, nombre, tipoComida, rangoPrecio, direccion, img):
        super().__init__(app)
        title_destino = ctk.CTkLabel(self, text=f'{nombre}', justify=tk.LEFT, font=('Helvetica', 20, 'bold'), anchor="w")
        title_destino.grid(row=0, column=0, padx=(50, 0))
        title_destino.configure(fg_color= '#E8DFDA', width=659, height=20, text_color='#23272d')
        card_destinos = ctk.CTkLabel(self, text=f'{tipoComida}\n{rangoPrecio}\n{direccion}\n{img}', justify=tk.LEFT, anchor="w", font=('Helvetica', 15))
        card_destinos.configure(fg_color='#E8DFDA', width=659, height=20, text_color='#23272d')
        card_destinos.grid(row=1, column=0, pady=(0, 0), padx=(50, 0))
        
        imagen_pil = Image.open(f'assets/img/{img}')
        img_width = 120
        img_height = 120
        imagen_pil = imagen_pil.resize((img_width, img_height))
        imagen_pil = self.round_corners(imagen_pil, radius=20)  # Redondear bordes
        imagen_tk = ImageTk.PhotoImage(imagen_pil)
        etiqueta_img = ctk.CTkLabel(self, image=imagen_tk, text='')
        etiqueta_img.image = imagen_tk
        etiqueta_img.grid(row=0, column=1, rowspan=2, pady=10, padx=10)
    
    #Para la imagen redondeada:
    def round_corners(self, pil_image, radius):
        circle = Image.new('L', (radius * 2, radius * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
        alpha = Image.new('L', pil_image.size, 255)
        w, h = pil_image.size
        alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
        alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
        alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
        alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
        pil_image.putalpha(alpha)
        return pil_image