import pandas as pd



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('./dataset/seguridad_sucio.csv')

  
#print(df.isnull().mean() * 100 )

#dimension filas x columnas
#print(df.shape)

#primera y ultima fila
#df.head(10)
#df.tail(5)

#tipos de datos
#print(df.dtypes)

# Resumen general: nulos, tipos, memoria
#df.info()

# Estadísticas numéricas
#print(df.describe())

# Estadísticas para columnas de texto también
#print(df.describe(include="all"))




#nulos por columna
#print(df.isnull().sum())

#mejor forma de sacar porcentaje de nulos por columna
#print((df.isnull().mean() * 100).round(2))


##aca empieza el trabajo

##conocer el dataset, primer vistado con los datos que trabajaremos
#print(df.head(10))

##tipos de datos con los que trabajaremos
#print(df.dtypes)

##porcentaje de nulos por columna
#print((df.isnull().mean() * 100).round(2))

##filas duplicadas
#print(df.duplicated().sum())

#borrar columnas que no aportan valor, que tienen muchos nulos, o que no son relevantes para el análisis
df = df.drop(columns=['observacion_manual', 'codigo_temp_x', 'id_old', 'id_seguridad'])



#print(df.isnull().mean() * 100)
#print(df.head(10))


#trabajar con las fechas


#convertir a formato datetime, esto limpia casi todos los problemas y datos raros
df['fecha'] = pd.to_datetime(
    df['fecha'],
    format='mixed',
    errors='coerce'
) 




##limpiar comuna

#vistazo inical


#borrado a travez de diccionario
basura_regex = r'(?i)^[^a-z0-9]*$|^error$|^nan$|^n/a$|^na$|^null$|^none$|^undefined$|^unknown$|^sin dat[os]*$|^no data$|^no disponible$|^desconocido$'

df['comuna'] = df['comuna'].str.strip().replace(basura_regex, pd.NA, regex=True)
diccionarioReemplazo = {
    'serena': 'la serena',
   'montepatria': 'monte patria'
}
##strip borra los espacios ne blancos y caracteres raros del principio y el final, lower pasa todo a minuscula para estandarizar
df['comuna'] = df['comuna'].replace(diccionarioReemplazo).str.lower()



#limpieza de tipo de delitos


#print(df['tipo_delito'].isnull().mean() * 100)


df['tipo_delito'] = df['tipo_delito'].str.strip().replace(basura_regex, pd.NA, regex=True).str.lower()

#sector
#print(df['sector'].head(100))
df['sector'] = df['sector'].str.strip().replace(basura_regex, pd.NA, regex=True).str.lower()

#print(df['cantidad_casos'].head(20).isnull().mean() * 100)
#coerce se encarga de todo para, es una bestia parda
df['cantidad_casos'] = pd.to_numeric(df['cantidad_casos'], errors='coerce')
#print(df['cantidad_casos'])


#gravedad 

# df.info(show_counts=True)
# print(df['gravedad'].isnull().mean() * 100)

df['gravedad'] = df['gravedad'].str.strip().replace(basura_regex, pd.NA, regex=True).str.lower()
##edad de los involucrados
df['edad_involucrado'] = pd.to_numeric(df['edad_involucrado'], errors='coerce').astype('Int64')
df.loc[df['edad_involucrado'] < 0, 'edad_involucrado'] = pd.NA


##comienzo de análisis exploratorio, con el dataset limpio y listo para trabajar

 
df['mes'] = df['fecha'].dt.month
df['mes_año'] = df['fecha'].dt.to_period('M')



#zonas de mayor riesgo
delitos_por_sector = df.groupby(['sector'])['cantidad_casos'].value_counts().unstack().fillna(0)
#print(delitos_por_sector)


#delitos por gravedad
delitos_por_gravedad = df.groupby('gravedad')['cantidad_casos'].sum().sort_values(ascending=False)
#print(delitos_por_gravedad)    


#tendencia delictual a lo largo del tiempo, por tipo de delito
tendencia_delictual = df.groupby(['mes_año', 'tipo_delito'])['cantidad_casos'].sum().unstack().fillna(0)
#print(tendencia_delictual)


## indicadpres claves

#delitos por comuna
delitos_por_comuna = df.groupby('comuna')['cantidad_casos'].sum().sort_values(ascending=False)
#print(delitos_por_comuna)

#evolucion mensual general
evolucion_mensual = df.groupby(df['mes_año'])['cantidad_casos'].sum()
#print(evolucion_mensual)

##delitos predomimantes
delitos_mas_comunes = df.groupby('tipo_delito')['cantidad_casos'].sum().sort_values(ascending=False)
#print(delitos_mas_comunes)






##lo que me pidio el brayatan


#delitos generales
delitos_generales = df.groupby('tipo_delito')['cantidad_casos'].sum().sort_values(ascending=False)
#print(delitos_generales)

#comunas mas afectadas
delitos_por_comuna = df.groupby('comuna')['cantidad_casos'].sum().sort_values(ascending=False)
#print(delitos_por_comuna)
tendencia_delictual.iloc[0]
#tipos de delito predominantes
delitos_mas_comunes = df.groupby('tipo_delito')['cantidad_casos'].sum().sort_values(ascending=False)
#print(delitos_mas_comunes)


#tendencia delictual a lo largo del tiempo, por tipo de delito
meses_incidencia = df.groupby('mes_año')['cantidad_casos'].sum().sort_values(ascending=False)
#print(tendencia_delictual)
#print(tendencia_delictual.index[0])
#print(tendencia_delictual.iloc[0])


#grupos etarios
limites = [0, 14, 17, 29, 59, 120]
nombres_grupos = ['Niños (0-14)', 'Adolescentes (15-17)', 'Jóvenes (18-29)', 'Adultos (30-59)', 'Adultos Mayores (60+)']

df['grupo_etario'] = pd.cut(df['edad_involucrado'], bins=limites, labels=nombres_grupos)
impacto_por_grupo = df.groupby('grupo_etario', observed=False)['cantidad_casos'].sum().sort_values(ascending=False)
#print(impacto_por_grupo)


##diccionario perron
dic = {
    "weas_del_brayan": {
        "delitos_generales": delitos_generales.to_dict(),
        "comunas_mas_afectadas": delitos_por_comuna.to_dict(),
        "tipos_de_delito_predominantes": delitos_mas_comunes.to_dict(),
        "tendencia_delictual_por_mes": tendencia_delictual.set_index(tendencia_delictual.index.astype(str)).to_dict(),
        "meses_con_mayor_incidencia": {
            "mes": str(tendencia_delictual.index[0]),
            "casos": float(tendencia_delictual.iloc[0].sum())
        },
 
        "impacto_por_grupo_etario": {str(k): v for k, v in impacto_por_grupo.to_dict().items()}
    }
}

import json

with open('reporte_seguridad.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=4)

print(dic)