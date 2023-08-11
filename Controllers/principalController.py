import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# Importación de vistas
from Views.inicioView import InicioView
from Views.resultadosBusquedaView import ResultadosBusquedaView
from Views.reviewsView import ReviewsVista
from Views.createReview import CreateReview
from Views.destinosView import DestinosView #agregado
from Views.actividadesView import VistaActividades #agregado
from Views.rutasView import VistaRutas
from Views.agregarARutasView import AgregarARutasView

# Importación de Modelos
from Models.reviews import Review
from Models.destinos import DestinoCulinario
from Models.reviews import Review
from Models.users import Usuario
from Models.actividades import Actividad
from Models.rutasVisitas import RutaDeVisita
from Models.ubicaciones import Ubicacion

from Controllers.controladorInicio import ControladorInicio
from Controllers.controladorReview import ControladorReview
from Controllers.controladorActividad import ControladorActividades 
from Controllers.controladorRutas import ControladorRutas
from Controllers.controladorDestinos import ControladorDestinos



class Aplicacion(ctk.CTk):  # le paso tk a la app para que tenga una interfas grafica
    def __init__(self):
        ctk.CTk.__init__(self)
        # a la interfas la paso la instancia para poder controlarla
        # y cambiarle cosas como el titutlo
        self.iconbitmap("assets/img/burger.ico")
        self.title("FoodApp")
        self.geometry("1080x720")
        self.config(bg='#F39116')
        self.resizable(False, False)  # Evita que los usuarios redimensionen la ventana
        self.inicializar()

        self.cambiar_frame(self.vista_inicio)       
    
    #Inicio la app
    def inicializar(self):
        ##CARGAR DATA
        destinos = DestinoCulinario.cargar_destinos("data/destinos.json")
        self.destinos = destinos
        reviews = Review.cargar_reviews("data/reviews.json")
        self.reviews = reviews
        usuarios = Usuario.cargar_users("data/usuarios.json")
        actividades = Actividad.cargar_actividades("data/actividades.json")
        self.actividades = actividades
        rutas = RutaDeVisita.cargar_rutas("data/rutas.json")
        self.rutas = rutas
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
        self.vista_inicio = InicioView(self, controladorInicio, destinos, ubicaciones)
        # A la vista de inicio le paso el controlador de su vista y la data de destinos.
        self.vista_resultados_busqueda = ResultadosBusquedaView(self, destinos, ubicaciones)
        self.vista_reviews = ReviewsVista(self, controladorReview, reviews, destinos, usuarios)
        self.vista_cargar_review = CreateReview(self, controladorReview, reviews, destinos, usuarios)
        self.vista_destinos = DestinosView(self, controladorDestinos, destinos, ubicaciones)
        self.vista_actividades = VistaActividades(self, controladorActividad, destinos, actividades)
        self.vista_rutas = VistaRutas(self, controladorRutas, destinos, actividades, rutas)
        self.vista_agregar_a_ruta = AgregarARutasView(self, controladorRutas, destinos, rutas)


        ##AJUSTES DE FRAMES
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_resultados_busqueda)
        self.ajustar_frame(self.vista_reviews)
        self.ajustar_frame(self.vista_cargar_review)
        self.ajustar_frame(self.vista_destinos)
        self.ajustar_frame(self.vista_actividades)
        self.ajustar_frame(self.vista_rutas)
        self.ajustar_frame(self.vista_agregar_a_ruta)


    # FUNCION PARA AJUSTAR LOS FRAMES
    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    # FUNCION PARA CAMBIAR LAS VIEWS
    def cambiar_frame(self, frame_destino):

        frame_destino.tkraise()

