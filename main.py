import tkinter as tk
from Controllers.principalController import ControladorPrincipal


root = tk.Tk()
root.title("Food Travel")
app = ControladorPrincipal(root)
root.mainloop()


