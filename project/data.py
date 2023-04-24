# from firstStep import df_parser , nota
# importando librerias necesarias
import re
import pandas as pd

# leyendo archivo excel con pandas
file_path = r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\ParserThea\Archivos\Captura Cliente Ejemplo.xlsx'
df = pd.read_excel(file_path)
df_parser = df.iloc[:, [0, 1, 2, 3, 4, 6, 7, 8]]

master_path = r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\ParserThea\Archivos\Maestro de Clientes (5).xlsx'
df_master = pd.read_excel(master_path, header=6)
df_master = df_master.iloc[:, [1, 3]]

# Definiendo la nota base
nota = 'THC-6104'

# Obteniendo el número de la nota base
nota_numero = int(re.findall('\d+', nota)[0])

# Obteniendo el texto de la nota base
texto = re.findall('[a-zA-Z.-]', nota)
nota_texto = ''
for letter in texto:
    nota_texto += letter

# Reemplazando el valor en la columna "Estatus Inventario" con "Cuarentena" si es que contiene esa palabra
for i in range(len(df_parser)):
    if 'Cuarentena' in df_parser.loc[i, 'Estatus Inventario']:
        df_parser.loc[i, 'Estatus Inventario'] = 'Cuarentena'

# Nueva columna 'Nombre Limpio'
df_parser['Nombre Limpio'] = ""

# Limpiando la columna 'Bill TO' y creando la columna 'Nombre Limpio'
for i in range(len(df_parser)):
    bill_to = df_parser.loc[i, 'Bill TO']
    clean_bill_to = re.sub(r'\(.*?\)', '', bill_to).strip().split(' ', 1)[1]
    df_parser.loc[i, 'Nombre Limpio'] = clean_bill_to

    # Buscando coincidencias entre columnas
    clientes = df_master[df_master['Nombre'].str.contains(clean_bill_to)]['Cliente'].tolist()
    if clientes:
        df_parser.loc[i, 'Codigo Cliente'] = clientes[0]

    # Creando la columna "Nota" y asignando valores basados en el valor en la columna "Estatus Inventario"
    estatus = df_parser.loc[i, 'Estatus Inventario']
    linea = df_parser.loc[i, 'Linea']
    if 'Cuarentena' in estatus:
        df_parser.loc[i, 'Nota'] = 'CUOT-' + nota_texto + str(nota_numero + 1)
    else:
        df_parser.loc[i, 'Nota'] = nota_texto + str(nota_numero + 1)

    if linea == 1:
        nota_numero += 1 # Agrega 1 al valor de nota_numero

# Imprimiendo las primeras filas del dataframe resultante
print(df_parser['Codigo Cliente'])
print(df_parser['Nombre Limpio'])
