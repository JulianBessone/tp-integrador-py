import json


class Review:
    def __init__(
        self, id_review, id_destino, id_usuario, calificacion, comentario, animo
    ):
        self.id = id_review
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def __str__(self):
        return f"""Review {self.id}: Destino ID: {self.id_destino},
    Usuario ID: {self.id_usuario}, Calificación: {self.calificacion}, 
    Comentario: {self.comentario}, Ánimo: {self.animo}"""

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_reviews(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Review.de_json(json.dumps(dato)) for dato in datos]

    @staticmethod
    def generate_id(archivo_json):
        try:
            with open(archivo_json, "r", encoding="utf-8") as archivo:
                reviews = json.load(archivo)
            # el maximo de los id de los reviews + 1
            return max([review["id_review"] for review in reviews]) + 1
        except FileNotFoundError:
            print(f"El archivo {archivo_json} no existe.")
            return None

    def add_to_json(self, archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            reviews = json.load(archivo)
        # antes de guardar el review cambiar id por id_review
        review = {
            "id_review": self.id,
            "id_destino": self.id_destino,
            "id_usuario": self.id_usuario,
            "calificacion": self.calificacion,
            "comentario": self.comentario,
            "animo": self.animo,
        }

        reviews.append(review)

        with open(archivo_json, "w", encoding="utf-8") as archivo:
            json.dump(reviews, archivo, indent=4, ensure_ascii=False)
