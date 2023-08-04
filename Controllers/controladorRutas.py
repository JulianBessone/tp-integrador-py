from Models.rutasVisitas import RutaDeVisita

class ControladorRutas:
    def __init__(self, app, destinos, rutas, actividades):
        self.app = app
        self.destinos = destinos #aca paso la lista de objetos destino
        self.rutas = rutas #paso la lista de las rutas.
        self.actividades = actividades #paso la lista de las actividades.
       

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)


    def agregar_ruta(self, nombre_ruta, ventana_nueva_ruta=None):
        if nombre_ruta:
            # Obtener el siguiente id disponible para la nueva ruta
            nuevo_id_ruta = len(self.rutas) + 1

            # Crear una nueva instancia de RutaDeVisita y agregarla a la lista de rutas
            nueva_ruta = RutaDeVisita(nuevo_id_ruta, nombre_ruta, [])
            self.rutas.append(nueva_ruta)

            # Si se proporciona una ventana Toplevel, ocultarla
            if ventana_nueva_ruta:
                ventana_nueva_ruta.destroy()

            return self.rutas


    def mostrar_informacion_destino(self, event):
        """
        Muestra los ingredientes y el tipo de cocina del destino 
        seleccionado en las etiquetas.
        """
        indice_seleccionado = self.app.vista_rutas.listbox_destinos.curselection()
        indice_seleccionado = indice_seleccionado[0]
        destino_seleccionado = self.destinos[indice_seleccionado] #objeto
        self.app.vista_rutas.destino_seleccionado = destino_seleccionado 


        tipo_cocina = destino_seleccionado.tipo_cocina
        nombre = destino_seleccionado.nombre
        self.app.vista_rutas.destino_label.config(text=f"{nombre}")
        self.app.vista_rutas.tipo_cocina_label.config(text=f"Tipo de cocina: {tipo_cocina}")

        # Obtener actividades del destino seleccionado
        actividades_destino = [actividad.nombre for actividad in self.actividades if actividad.destino_id == destino_seleccionado.id]
        # Actualizar etiqueta con las actividades del destino
        self.app.vista_rutas.actividades_label.config(text=f"Actividades: {', '.join(actividades_destino)}")


    def agregar_a_ruta(self):
        """
        Muestra una nueva ventana con las rutas del usuario. Al seleccionar debe
        agregar el destino seleccionado a la ruta.
        1 - Paso el termino a buscar
        2- muestro una nueva vista

        """        
        print('se presiono el boton agregar a ruta en la funcion')
        # Obtiene el término de búsqueda del input
        #termino_busqueda = input_buscar

        # Cambio la vista a la vista agregarARutasView
        self.app.cambiar_frame(self.app.vista_agregar_a_ruta)
        # Actualizo los resultados en base a lo que ingrese el user
        #self.app.vista_resultados_busqueda.actualizar_resultados(termino_busqueda)

    def seleccionar_ruta(self, event):
        pass

    def agregar_destino(self):
        print('guardar el destino')
        

