import tkinter as tk
from Views.inicioView import InicioView
from Views.resultadosBusquedaView import ResultadosBusquedaView
from tkinter import messagebox
from Models.reviews import Review
from Models.destinos import DestinoCulinario
from Models.users import Usuario
from Controllers.controladorInicio import ControladorInicio


class Aplicacion(tk.Tk):# le paso tk a la app para que tenga una interfas grafica
    def __init__(self):
        tk.Tk.__init__(self)# a la interfas la paso la instancia para poder controlarla y cambiarle cosas como el titutlo
        self.title('FoodApp')
        self.geometry("500x500")
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
        
        ##VISTAS
        self.vista_inicio = InicioView(self, controladorInicio, destinos)#A la vista de inicio le paso el controlador de su vista y la data de destinos.
        self.vista_resultados_busqueda = ResultadosBusquedaView(self, destinos)

        ##AJUSTES DE FRAMES
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_resultados_busqueda)

    #FUNCION PARA AJUSTAR LOS FRAMES
    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    #FUNCION PARA CAMBIAR LAS VIEWS
    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()
    