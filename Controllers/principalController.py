from models.reviews import Review

class ControladorPrincipal:
    def __init__(self):
        self.reviews = Review.cargar_reviews("app/data/locales.json")
        self.marcadores = []
        self.imagenes = []
        self.cargar_reviews()

        
    def cargar_reviews(self):
        for review in self.reviews:
            pass

app = ControladorPrincipal()

print(app.reviews)