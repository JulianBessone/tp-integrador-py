from utils import objetos_a_json

class Review:
    def __init__(self, id_review, id_destino, id_usuario, calificacion, comentario, animo):
        self.id = id_review
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def __str__(self):
        return f"Review {self.id}: Destino ID: {self.id_destino}, Usuario ID: {self.id_usuario}, Calificación: {self.calificacion}, Comentario: {self.comentario}, Ánimo: {self.animo}"

review1 = Review(1, 1, 1, 4, "La pasta estaba deliciosa.", "Positivo")
review2 = Review(2, 2, 2, 3, "El servicio fue lento.", "Negativo")
review3 = Review(3, 1, 2, 5, "Increíble experiencia gastronómica.", "Positivo")
review4 = Review(4, 3, 3, 2, "La comida no fue lo que esperaba.", "Negativo")
review5 = Review(5, 2, 4, 4, "Recomiendo el vino tinto.", "Positivo")
review6 = Review(6, 4, 1, 1, "No volvería a este lugar.", "Negativo")

listaReviews = (review1,review2,review3,review4,review5,review6)
listaReviewsJSON = objetos_a_json(listaReviews)