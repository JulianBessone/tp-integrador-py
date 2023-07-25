from Views.inicioView import InicioView
from Views.resultadosBusquedaView import ResultadosBusquedaView
from tkinter import messagebox
from Models.reviews import Review
from Models.destinos import DestinoCulinario
from Models.users import Usuario

class ControladorPrincipal:
    def __init__(self, root):
        self.reviews = Review.cargar_reviews("data/reviews.json")
        self.destinos = DestinoCulinario.cargar_destinos("data/destinos.json")
        self.usuarios = Usuario.cargar_users("data/usuarios.json")
        self.vista = InicioView(root, self.destinos)
        self.marcadores = []
        self.imagenes = []
        self.cargar_reviews()

        
    def cargar_reviews(self):
        for review in self.reviews:
            pass

    