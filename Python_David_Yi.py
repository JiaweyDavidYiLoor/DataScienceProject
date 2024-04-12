import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Telco-Customer-tvc.csv', sep=';')

print(df.head())

#PREGUNTA1
#Se conviernte a número y lo que no sea número a NaN para filtra aún mejor la data
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Se verifica si TotalCharges tiene valores NaN o 0
df_totalcharges_0 = df[df['TotalCharges'].isna() | (df['TotalCharges'] == 0)]

# Visualizamos el filtro
print(df_totalcharges_0.head(20))
print(df_totalcharges_0[['InternetService', 'TotalCharges']].head(10))


# Filtrar los clientes que tienen InternetService diferente de 'No' es decir los activos
df_activos = df[df['InternetService'] != 'No']

# Calcular el promedio de TotalCharges para cada tipo de InternetService
promedio_por_internet_service = df_activos.groupby('InternetService')['TotalCharges'].mean().reset_index()

# Renombrar la columna de promedios para poder visualizar de mejor manera el resultado y redondeamos a 2 decimales
promedio_por_internet_service.rename(columns={'TotalCharges': 'Promedio de TotalCharges'}, inplace=True)
promedio_por_internet_service['Promedio de TotalCharges'] = promedio_por_internet_service['Promedio de TotalCharges'].round(2)

print(promedio_por_internet_service)

#PREGUNTA2
# Filtrar los clientes que han desertado (CHURN = 'Yes')
df_churn = df[df['Churn'] == 'Yes']
print(len(df_churn))

# Valor máximo de TotalCharges
maximo_totalcharges = df_churn['TotalCharges'].max()

# Valor mínimo de TotalCharges
minimo_totalcharges = df_churn['TotalCharges'].min()

print("Valor máximo de TotalCharges:", maximo_totalcharges)
print("Valor mínimo de TotalCharges:", minimo_totalcharges)


df_churn_no = df[df['Churn'] == 'No']
print(len(df_churn_no))

print(str(len(df_churn)+len(df_churn_no)))

# Filtrar los clientes que han desertado (CHURN = 'Yes')
df_churn = df[df['Churn'] == 'Yes']
print(len(df_churn))

# Valor máximo de TotalCharges
maximo_totalcharges = df_churn['TotalCharges'].max()

# Valor mínimo de TotalCharges
minimo_totalcharges = df_churn['TotalCharges'].min()

# Calcular la media, mediana y desviación estándar de TotalCharges para los clientes que han desertado
media_totalcharges = df_churn['TotalCharges'].mean().round(2)
mediana_totalcharges = df_churn['TotalCharges'].median().round(2)
desviacion_totalcharges = df_churn['TotalCharges'].std().round(2)

# Calcular el rango intercuartílico (IQR) de TotalCharges para los clientes que han desertado
q1 = df_churn['TotalCharges'].quantile(0.25).round(2)
q3 = df_churn['TotalCharges'].quantile(0.75).round(2)
iqr_totalcharges = q3 - q1

# Imprimir los resultados
print("Estadísticas descriptivas para TotalCharges de los clientes que han desertado:")
print("Media:", media_totalcharges)
print("Mediana:", mediana_totalcharges)
print("Desviación estándar:", desviacion_totalcharges)
print("Rango intercuartílico (IQR):", iqr_totalcharges)


#PREGUNTA3
# Obtener los valores únicos y contar la frecuencia de cada valor en la columna "PaymentMethod"
conteo_metodos_pago = df_churn_no['PaymentMethod'].value_counts()

# Suma de todos los registros
total_registros = conteo_metodos_pago.sum()

print("Valores únicos en la columna 'PaymentMethod' y su frecuencia:")
print(conteo_metodos_pago)

print("\nTotal de registros:", total_registros)


#PREGUNTA4
# Filtrar los clientes con algún servicio de streaming en df_churn
clientes_con_streaming = df_churn[(df_churn['StreamingTV'] == 'Yes') | (df_churn['StreamingMovies'] == 'Yes')]
print("Número total de clientes con algún servicio de streaming:", len(clientes_con_streaming))

# Contar el número total de clientes que desertaron en df_churn
total_clientes_desertaron = len(df_churn)
print("Número total de clientes que desertaron:", total_clientes_desertaron)

# Contar el número de clientes con streaming
total_clientes_con_streaming = len(clientes_con_streaming)
print("Número total de clientes que desertaron y tenían algún servicio de streaming:", total_clientes_con_streaming)

# Calcular el porcentaje de clientes que desertaron y tenían algún servicio de streaming
porcentaje_clientes_con_streaming = (total_clientes_con_streaming / total_clientes_desertaron) * 100
porcentaje_clientes_con_streaming = round(porcentaje_clientes_con_streaming, 2)
print("Porcentaje de clientes que desertaron y tenían algún servicio de streaming:", porcentaje_clientes_con_streaming, "%")



#PREGUNTA6

# Agrupar los datos por las variables "Churn" y "Contract" y contar el número de registros en cada grupo
grupo_contrato_churn = df.groupby(['Churn', 'Contract']).size().unstack()

# Graficar los resultados 
grupo_contrato_churn.plot(kind='bar', stacked=True, figsize=(10, 8), color=['yellow','blue', 'purple'])
plt.title('Distribución de contratos para cada categoría de churn')
plt.xlabel('Churn')
plt.ylabel('Número de clientes')
plt.xticks(rotation=0)  
plt.legend(title='Contract')
plt.show()

#PREGUNTA7
# Ordenar primero por monto de TotalCharges en orden descendente y luego por antigüedad (tenure) en orden descendente
top_10_clientes_activos = df_churn_no.sort_values(by=['TotalCharges', 'tenure'], ascending=[False, False]).head(10)

# Mostrar el DataFrame resultante
print(top_10_clientes_activos)


#PREGUNTA8
# Contar el número de clientes que tienen cada servicio

total_clientes = len(df_churn_no)

total_clientes_con_internet = (df_churn_no['InternetService'] != 'No').sum()
porc_int = (total_clientes_con_internet / total_clientes) * 100

total_clientes_con_telephone = (df_churn_no['PhoneService'] == 'Yes').sum()
porc_tel = (total_clientes_con_telephone / total_clientes) * 100

total_clientes_con_StreamingTv = (df_churn_no['StreamingTV'] == 'Yes').sum()
porc_Str_TV = (total_clientes_con_StreamingTv / total_clientes) * 100

total_clientes_con_StreamingMovies = (df_churn_no['StreamingMovies'] == 'Yes').sum()
porc_Str_Mov = (total_clientes_con_StreamingMovies / total_clientes) * 100

# Mostrar el resultado
print("Porcentaje de clientes con servicio de Internet:", porc_int)
print("Porcentaje de clientes con servicio de Telefonía:", porc_tel)
print("Porcentaje de clientes con servicio de Streaming TV:", porc_Str_TV)
print("Porcentaje de clientes con servicio de Streaming Movies:", porc_Str_Mov)


