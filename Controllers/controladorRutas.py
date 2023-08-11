from Models.rutasVisitas import RutaDeVisita
from tkinter import messagebox
from datetime import datetime
import json
from PIL import Image, ImageTk

class ControladorRutas:
    def __init__(self, app, destinos, rutas, actividades):
        self.app = app
        self.destinos = destinos #aca paso la lista de objetos destino
        self.rutas = rutas #paso la lista de las rutas.
        self.actividades = actividades #paso la lista de las actividades.
        self.destino_seleccionado = {}
       

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def regresar_rutas(self):
        self.app.cambiar_frame(self.app.vista_rutas)        


    def mostrar_informacion_destino(self, event):
        """
        Muestra los ingredientes y el tipo de cocina del destino 
        seleccionado en las etiquetas.

        """
        indice_seleccionado = self.app.vista_rutas.listbox_destinos.curselection()
        if len(indice_seleccionado) > 0:
            indice_seleccionado = indice_seleccionado[0] #ese es el indice de la lista
        else:
            return
        #recupero el nombre del destino
        nombre_destino_seleccionado = self.app.vista_rutas.listbox_destinos.get(indice_seleccionado)
        #con el nombre del destino recuperar el id del destino
        for destino in self.destinos:
            if destino.nombre == nombre_destino_seleccionado:
                #print("destino: ", destino.id, " ", destino.nombre, " ", destino.tipo_cocina, " ", destino.popularidad)
                self.destino_seleccionado = destino

        self.app.vista_rutas.destino_seleccionado = self.destino_seleccionado 


        tipo_cocina = self.destino_seleccionado.tipo_cocina
        nombre = self.destino_seleccionado.nombre
        self.app.vista_rutas.destino_label.configure(text=f"{nombre}")
        self.app.vista_rutas.tipo_cocina_label.configure(text=f"{tipo_cocina}")

        # Obtener actividades del destino seleccionado
        #actividades_destino = [actividad.nombre for actividad in self.actividades if actividad.destino_id == self.destino_seleccionado.id]

        actividades_destino=""

        for actividad in self.actividades:
            if actividad.destino_id == self.destino_seleccionado.id:
                # Convertir la fecha a un objeto datetime
                fecha_hora_obj = datetime.strptime(actividad.hora_inicio, "%Y-%m-%dT%H:%M:%S")
                # Formatear la fecha en formato dd/mm/aaaa
                fecha = fecha_hora_obj.strftime("%d/%m/%Y")
                # Formatear la hora en formato hh:mm
                hora = fecha_hora_obj.strftime("%H:%M")            
                actividades_destino = actividades_destino + f"{fecha} - {hora} \n{actividad.nombre}\n\n"

        # Actualizar etiqueta con las actividades del destino
        if actividades_destino =='':
            actividades_destino ='No hay actividades programadas'
        self.app.vista_rutas.actividades_label.configure(text=f"{actividades_destino}")

        # Obtener la URL de la imagen del destino desde el JSON
        imagen_url = self.destino_seleccionado.imagen
        self.app.vista_rutas.cargar_imagen(imagen_url)



    def agregar_a_ruta(self, destino_seleccionado):
        """
        Muestra una nueva ventana con las rutas del usuario. Al seleccionar debe
        agregar el destino seleccionado a la ruta.
        """        
        # Cambio la vista a la vista agregarARutasView
        if not destino_seleccionado:
            messagebox.showinfo("Aviso", "Seleccione un destino.")
            return
        self.app.cambiar_frame(self.app.vista_agregar_a_ruta)
        self.app.vista_agregar_a_ruta.titulo.configure(text=f"Destino seleccionado: {self.destino_seleccionado.nombre}")
        self.app.destino_seleccionado = destino_seleccionado



    def agregar_destino(self, ruta_seleccionada):
        ruta = ruta_seleccionada
        # print('Destino objeto: ', self.destino_seleccionado.id, " nombre: ", self.destino_seleccionado.nombre )
        # print('Ruta Seleccionada: ', ruta.nombre)

        # Verificar si el destino ya está en la ruta
        if self.destino_seleccionado.id in ruta.destinos:
            #print("El destino ya se encuentra en la ruta.")
            messagebox.showinfo("Aviso", "El destino ya se encuentra en la ruta.")
            return
   
        # Buscar la ruta seleccionada en la lista de rutas
        for r in self.rutas:
            if r.id == ruta.id:
                # Agregar el ID del destino seleccionado a la lista de destinos de la ruta
                r.destinos.append(self.destino_seleccionado.id)
                break  # Romper el ciclo después de encontrar la ruta
        
        # Actualizar el archivo rutas.json
        with open('data/rutas.json', 'w') as json_file:
            rutas_data = []
            for r in self.rutas:
                rutas_data.append({
                    "id_ruta": r.id,
                    "nombre_ruta": r.nombre,
                    "destinos": r.destinos
                })
            json.dump(rutas_data, json_file, indent=4)

        # Imprimir mensaje de éxito o realizar otras acciones
        #print('Destino agregado a la ruta:', self.destino_seleccionado.nombre)
        messagebox.showinfo("Aviso", "El destino fue agregado a tu ruta.")


        #ESTO NO FUNCIONA!!
        self.app.vista_agregar_a_ruta.cargarDestinosRuta(ruta_seleccionada)


    def agregar_ruta_a_json(self, nueva_ruta):
        # Leer el contenido actual del archivo rutas.json
        with open('data/rutas.json', 'r') as archivo:
            datos_rutas = json.load(archivo)

        # Agregar la nueva ruta a la lista de rutas
        datos_rutas.append({
            "id_ruta": nueva_ruta.id,
            "nombre_ruta": nueva_ruta.nombre,
            "destinos": nueva_ruta.destinos
        })

        # Escribir los datos actualizados de nuevo en el archivo
        with open('data/rutas.json', 'w') as archivo:
            json.dump(datos_rutas, archivo, indent=4)


    def guardar_ruta(self, nombre_ruta):
        # Crear una nueva instancia de RutaDeVisita y agregarla a la lista de rutas
        nueva_ruta = RutaDeVisita(len(self.rutas) + 1, nombre_ruta, [])
        self.rutas.append(nueva_ruta)

        # Llamar a la función para agregar la nueva ruta al archivo JSON
        self.agregar_ruta_a_json(nueva_ruta)



        

