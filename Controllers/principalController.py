import tkinter as tk
from tkinter import messagebox
#Importación de vistas
from Views.inicioView import InicioView
from Views.resultadosBusquedaView import ResultadosBusquedaView
from Views.reviewsView import ReviewsVista

from Views.destinosView import DestinosView #agregado
from Views.actividadesView import VistaActividades #agregado
from Views.rutasView import VistaRutas

#Importación de Modelos
from Models.destinos import DestinoCulinario
from Models.reviews import Review
from Models.users import Usuario
from Models.actividades import Actividad
from Models.rutasVisitas import RutaDeVisita
from Models.ubicaciones import Ubicacion



#Importación de Controladores
from Controllers.controladorInicio import ControladorInicio
from Controllers.controladorReview import ControladorReview
from Controllers.controladorDestino import ControladorDestinos #agregado
from Controllers.controladorActividad import ControladorActividades #agregado
from Controllers.controladorRutas import ControladorRutas
from Controllers.controladorDestinos import ControladorDestinos


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
        rutas = RutaDeVisita.cargar_rutas("data/rutas.json")
        ubicaciones = Ubicacion.cargar_ubicaciones("data/ubicacion.json")
        self.ubicaciones = ubicaciones
       
        
        ##CONTROLADORES
        controladorInicio = ControladorInicio(self)
        controladorReview = ControladorReview(self)
        controladorDestinos = ControladorDestinos(self, destinos)
        controladorInicio = ControladorInicio(self)
        controladorReview = ControladorReview(self)
        controladorActividad = ControladorActividades(self, destinos, actividades)
        controladorRutas = ControladorRutas(self, destinos, rutas, actividades)
        
        ##VISTAS
        self.vista_inicio = InicioView(self, controladorInicio, destinos)#A la vista de inicio le paso el controlador de su vista y la data de destinos.
        self.vista_resultados_busqueda = ResultadosBusquedaView(self, destinos)
        self.vista_reviews = ReviewsVista(self, controladorReview, reviews)
        self.vista_destinos = DestinosView(self, controladorDestinos, destinos, ubicaciones)
        self.vista_actividades = VistaActividades(self, controladorActividad) #agregado
        self.vista_rutas = VistaRutas(self, controladorRutas)


        ##AJUSTES DE FRAMES
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_resultados_busqueda)
        self.ajustar_frame(self.vista_reviews)
        self.ajustar_frame(self.vista_destinos) #agregado
        self.ajustar_frame(self.vista_actividades) #agregado
        self.ajustar_frame(self.vista_rutas) #agregado



    #FUNCION PARA AJUSTAR LOS FRAMES
    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    #FUNCION PARA CAMBIAR LAS VIEWS
    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()