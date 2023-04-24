import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sys

# Crea una ventana emergente para que el usuario seleccione el archivo
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Selecciona un archivo de Excel", filetypes=(("Archivo de Excel", "*.xlsx"),))

df = pd.read_excel(file_path, header=1)
df_parser = df.iloc[:, [0, 1, 2, 3, 4, 6, 7, 8]]

print("Ultima nota:")
nota= input()
## Crea una ventana emergente para que el usuario ingrese la primera nota
#nota = ""
#def get_nota():
#    global nota
#    global file_path
#    nota = entry_nota.get()
#    root_nota.destroy()
#
#    # Lee el archivo de Excel seleccionado con pandas
#    df = pd.read_excel(file_path, header=1)
#
#    # Selecciona solo las columnas necesarias
#    df_parser = df.iloc[:, [0, 1, 2, 3, 4, 6, 7, 8]]
#
#    print(nota)
#    print(len(df_parser.keys()))
#
#
#    sys.exit()
#
#
#
#root_nota = tk.Toplevel()
#root_nota.geometry("200x100") # Agrega esta línea para especificar el tamaño
#label_nota = tk.Label(root_nota, text="Ingresa la primera nota:")
#entry_nota = tk.Entry(root_nota)
#button_nota = tk.Button(root_nota, text="Aceptar", command=get_nota)
#
#label_nota.pack()
#entry_nota.pack()
#button_nota.pack()
#
#root_nota.mainloop()
