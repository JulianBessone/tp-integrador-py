import tkinter as tk

class ControladorDestinos:
    def __init__(self, app):
        self.app = app
        self.marcadores = []

        self.cargar_marcadores()

    def cargar_marcadores(self):
        for ubicacion in (self.app.ubicaciones):
            marcador = self.app.vista_destinos.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud)
            self.marcadores.append(marcador)
