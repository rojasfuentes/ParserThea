from loadCaptura import file_path , master_path, nota
import re
import pandas as pd

# TEST : Nota
#nota = 'THC-6104'
# TEST: df_parser
#file_path = r'C:\Users\JFROJAS\Desktop\PARSER\Thea\Archivos\Captura Cliente Ejemplo.xlsx'
df = pd.read_excel(file_path)
df_parser = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8]]


# Master de clientes
#master_path = r'C:\Users\JFROJAS\Desktop\PARSER\Thea\Archivos\Maestro de Clientes (5).xlsx'
df_master = pd.read_excel(master_path, header=6)
df_master = df_master.iloc[:, [1, 3]]

#Separo el número de la nota del texto
nota_numero = int(re.findall('\d+', nota)[0])
texto = re.findall('[a-zA-Z.-]', nota)
nota_texto = ''
for letter in texto:
    nota_texto += letter

# Remplazo los valores en la columna 'Estatus Inventario' por 'Cuarentena'
for i in range(len(df_parser)):
    if 'Cuarentena' in df_parser.loc[i, 'Estatus Inventario']:
        df_parser.loc[i, 'Estatus Inventario'] = 'Cuarentena'


for i in range(len(df_parser)):
    # Creando la columna "Nota" y asignando valores basados en el valor en la columna "Estatus Inventario"
    linea = df_parser.loc[i, 'Linea']
    estatus = df_parser.loc[i, 'Estatus Inventario']
    if linea == 1:
        nota_numero += 1 # Agrega 1 al valor de nota_numero
    if 'Cuarentena' in estatus:
        df_parser.loc[i, 'Nota'] = 'COMP-' + nota_texto + str(nota_numero + 1)
    else:
        df_parser.loc[i, 'Nota'] = nota_texto + str(nota_numero + 1)



# Copiar la primera palabra de cada elemento en la columna 'Bill TO' , el primero aún tiene el guión
df_parser['Codigo'] = df_parser['Bill TO'].str.split().str[0]
df_parser['Codigo2'] = df_parser['Codigo'].str.replace('-', '')


# Crear una nueva columna 'Codigo Cliente' en el DataFrame df_parser
df_parser['Codigo Cliente'] = ''

# Codigo Cliente
for i, row in df_parser.iterrows():
    codigo = row['Codigo2']
    exception = row['Codigo']
    mask = df_master['Cliente'].str.contains(codigo)
    if mask.any():
        df_parser.loc[i, 'Codigo Cliente'] = df_master.loc[mask, 'Cliente'].iloc[0]
    else:
        df_parser.loc[i, 'Codigo Cliente'] = exception



#print(df_parser.keys())
df = df_parser.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]]
print(df.keys())