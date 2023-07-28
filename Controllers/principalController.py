import tkinter as tk
from tkinter import messagebox
#Importación de vistas
from Views.inicioView import InicioView
from Views.resultadosBusquedaView import ResultadosBusquedaView
from Views.reviewsView import ReviewsVista
#Importación de Modelos
from Models.reviews import Review
from Models.destinos import DestinoCulinario
from Models.users import Usuario
#Importación de Controladores
from Controllers.controladorInicio import ControladorInicio
from Controllers.controladorReview import ControladorReview

class Aplicacion(tk.Tk):# le paso tk a la app para que tenga una interfas grafica
    def __init__(self):
        tk.Tk.__init__(self)# a la interfas la paso la instancia para poder controlarla y cambiarle cosas como el titutlo
        self.iconbitmap('assets/img/burger.ico')
        self.title('FoodApp')
        self.geometry("1080x720")
        self.resizable(True, True)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)
    
    #Inicio la app
    def inicializar(self):
        ##CARGAR DATA
        destinos = DestinoCulinario.cargar_destinos("data/destinos.json")
        reviews = Review.cargar_reviews("data/reviews.json")
        usuarios = Usuario.cargar_users("data/usuarios.json")

        ##CONTROLADORES
        controladorInicio = ControladorInicio(self)
        controladorReview = ControladorReview(self)
        
        ##VISTAS
        self.vista_inicio = InicioView(self, controladorInicio, destinos)#A la vista de inicio le paso el controlador de su vista y la data de destinos.
        self.vista_resultados_busqueda = ResultadosBusquedaView(self, destinos)
        self.vista_reviews = ReviewsVista(self, controladorReview, reviews)
  

        ##AJUSTES DE FRAMES
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_resultados_busqueda)
        self.ajustar_frame(self.vista_reviews)

    #FUNCION PARA AJUSTAR LOS FRAMES
    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    #FUNCION PARA CAMBIAR LAS VIEWS
    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()
    