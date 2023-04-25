import tkinter as tk
from tkinter import filedialog
import pandas as pd
import PySimpleGUI as sg

# Define la ventana emergente
layout = [[sg.Text('Ingresa la nota:'), sg.InputText()],[sg.Button('Ok')]]

# Crea la ventana
window = sg.Window('Ingresar nota', layout)

# Loop para leer los eventos y datos de entrada
while True:
    event, values = window.read()
    if event == 'Ok':
        nota = values[0]
        break

# Cierra la ventana
window.close()

# Imprime la nota ingresada
print("Ultima nota:", nota)


file_path = filedialog.askopenfilename(title="Selecciona 'Captura Cliente'", filetypes=(("Archivo de Excel", "*.xlsx"),))
master_path = filedialog.askopenfilename(title="Selecciona Maestro de clientes", filetypes=(("Archivo de Excel", "*.xlsx"),))
store_path = filedialog.askopenfilename(title="Selecciona Consulta Inventario", filetypes=(("Archivo de Excel", "*.xlsx"),))

df = pd.read_excel(file_path)



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
