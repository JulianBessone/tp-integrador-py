"""
FUNCION PARA TRANSFORMAR UNA LISTA DE OBJETOS A UNA LISTA DE OBJETOS JSON
"""
def usuarios_a_json(lista_usuarios):
    usuarios_json = []
    for usuario in lista_usuarios:
        usuario_dict = {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "historial_rutas": usuario.historial_rutas
        }
        usuarios_json.append(usuario_dict)
    return usuarios_json

def objetos_a_json(lista):
    resultadoLista = []
    for object in lista:
        obj = {}
        atributos = vars(object)
        for atributo, valor in atributos.items():
            obj[atributo] = valor
        resultadoLista.append(obj)
    print(resultadoLista)