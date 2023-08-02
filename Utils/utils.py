"""
FUNCION PARA TRANSFORMAR UNA LISTA DE OBJETOS A UNA LISTA DE OBJETOS JSON
"""


def objetos_a_json(lista):
    resultadoLista = []
    for object in lista:
        obj = {}
        atributos = vars(object)
        for atributo, valor in atributos.items():
            obj[atributo] = valor
        resultadoLista.append(obj)
    print(resultadoLista)
