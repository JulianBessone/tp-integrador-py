from reviews import listaReviewsJSON

def ver_reviews():
    return print(listaReviewsJSON)

def escribir_review(objeto):
    listaReviewsJSON.append(objeto)
    return print(listaReviewsJSON)

