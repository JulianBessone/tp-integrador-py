import json

def verReviews():
    with open('../Data/reviews.JSON') as archivo:
        datos = json.load(archivo)
    print(datos)

verReviews()