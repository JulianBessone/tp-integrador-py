from Controllers.principalController import Aplicacion

"""Creo una instancia de Aplicacion, en ella se cargaran: la data, los controladores y las vistas"""
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()