import tkinter as tk
from tkinter import messagebox
#Importación de vistas
from Views.inicioView import InicioView
from Views.resultadosBusquedaView import ResultadosBusquedaView
from Views.reviewsView import ReviewsVista
from Views.destinosView import VistaDestinos #agregado
from Views.actividadesView import VistaActividades #agregado
#Importación de Modelos
from Models.reviews import Review
from Models.destinos import DestinoCulinario
from Models.users import Usuario
from Models.actividades import Actividad #agregado
#Importación de Controladores
from Controllers.controladorInicio import ControladorInicio
from Controllers.controladorReview import ControladorReview
from Controllers.controladorDestino import ControladorDestinos #agregado
from Controllers.controladorActividad import ControladorActividades #agregado

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
        actividades = Actividad.cargar_actividades("data/actividades.json") #agregado


        ##CONTROLADORES
        controladorInicio = ControladorInicio(self)
        controladorReview = ControladorReview(self)
        controladorDestino = ControladorDestinos(self, destinos) #agregado
        controladorActividad = ControladorActividades(self, actividades) #agregado

        
        ##VISTAS
        self.vista_inicio = InicioView(self, controladorInicio, destinos)#A la vista de inicio le paso el controlador de su vista y la data de destinos.
        self.vista_resultados_busqueda = ResultadosBusquedaView(self, destinos)
        self.vista_reviews = ReviewsVista(self, controladorReview, reviews)
        self.vista_destinos = VistaDestinos(self, controladorDestino) #agregado
        self.vista_actividades = VistaActividades(self, controladorActividad) #agregado
  

        ##AJUSTES DE FRAMES
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_resultados_busqueda)
        self.ajustar_frame(self.vista_reviews)
        self.ajustar_frame(self.vista_destinos) #agregado
        self.ajustar_frame(self.vista_actividades) #agregado

    #FUNCION PARA AJUSTAR LOS FRAMES
    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    #FUNCION PARA CAMBIAR LAS VIEWS
    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()
    