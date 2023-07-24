from utils import objetos_a_json

class RutaVisita:
    def __init__(self, id_ruta, nombre, destinos):
        self.id = id_ruta
        self.nombre = nombre
        self.destinos = destinos

    def __str__(self):
        return f"Ruta de Visita: {self.nombre}, ID: {self.id}, Destinos: {self.destinos}"

# Ejemplo de uso
ruta1 = RutaVisita(1, "Tour Gastronómico", [1, 2, 4])
ruta2 = RutaVisita(2, "Ruta de Vinos", [2, 3])
ruta3 = RutaVisita(3, "Ruta Cultural", [1, 3, 4])
ruta4 = RutaVisita(4, "Ruta De Empanadas", [2, 3, 1])
ruta5 = RutaVisita(5, "Ruta De Parrillas", [1, 3, 4])
ruta6 = RutaVisita(6, "Ruta De Carritos Sandwicheros", [1, 3, 4])

listaRutasVisitas = (ruta1,ruta2,ruta3,ruta4,ruta5,ruta6)
listaRutasVisitasJSON = objetos_a_json(listaRutasVisitas)



