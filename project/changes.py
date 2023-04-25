#from loadCaptura import store_path
from master import df
import pandas as pd

store_path = r'C:\Users\JFROJAS\Desktop\PARSER\Thea\Archivos\Consulta de Inventario 18-04-23.xlsx'
df_store = pd.read_excel(store_path, header=4)
df_store = df_store.iloc[:, [0, 1, 3, 6]]

for i in range(len(df)):
    codigo_producto = df.loc[i, 'Codigo Producto']
    for j in range(len(df_store)):
        if codigo_producto == df_store.loc[j, 'Artículo']:
            lote = df.loc[i, 'Lote']
            lote_store = df_store.loc[j, 'Lote']
            if lote == lote_store:
                estatus = df_store.loc[j, 'Estatus']
                if 'Menor' in str(estatus):
                    ubicacion = df_store.loc[j, 'Ubicación']
                    df.loc[i:i, 'Ubicacion'] = ubicacion
                break

df_final = df.iloc[:, [9, 2, 3, 4, 5, 6, 7, 8, 11]]
df_final.to_excel(r'C:\Users\JFROJAS\Desktop\PARSER\Thea/modificaciones.xlsx', index=False)

