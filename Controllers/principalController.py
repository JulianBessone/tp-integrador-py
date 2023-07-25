from Models.reviews import Review

class ControladorPrincipal:
    def __init__(self):
        self.reviews = Review.cargar_reviews("data/reviews.json")
        self.marcadores = []
        self.imagenes = []
        self.cargar_reviews()

        
    def cargar_reviews(self):
        for review in self.reviews:
            pass

