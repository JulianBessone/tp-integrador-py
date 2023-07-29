import tkinter as tk


class VistaActividades(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de las actividades del destino culinario.
        """
        super().__init__(master)
        self.master = master #le paso la aplicacion
        self.controlador = controlador  #le paso el controlador de actividad
        self.destino_label = tk.Label(self, text="")
        self.destino_label.pack(pady=50)
        self.destino_label.config(justify=tk.LEFT)
        self.boton_regresar = tk.Button(
            self,
            text="Regresar a la lista de destinos",
            command=self.controlador.regresar_destinos,
        )
        self.boton_regresar.pack(pady=10)

    def mostrar_actividades_destino(self, destino):  
        """
        el parametro destino que recibe es la instancia del objeto
        Muestra la información del destino recibido como parámetro.
        """        
        info = f"Destino: {destino.id} - {destino.nombre}"
        info_actividad = ""


        actividades = self.controlador.obtener_actividades_destino(destino.id)
        ##self.listbox.delete(0, tk.END)
        for actividad in actividades:
            ##self.listbox.insert(tk.END, actividad.nombre)
            info_actividad = info_actividad + f"\nActividad: {actividad.nombre} - Inicia a las: {actividad.hora_inicio}"

        self.destino_label["text"] = info + info_actividad


      
