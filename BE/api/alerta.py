# -*- coding: utf-8 -*-
"""meteo_cracks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B0yhFHCVd__FFjtlo_XTyKZuExNRNp3m
"""

import pandas as pd



meli = '/content/drive/MyDrive/Globant AI/meteo - Sheet 1.csv'
df = pd.read_csv("api/static/meteo2.csv")

df.head()

df.isnull().sum() / len(df) * 100

df.columns

df = df[df['Disaster Subgroup'] != 'Geophysical']
df.head()

sum(df['Start Month'] == df['End Month'])

df['Start Day'].fillna(1, inplace=True)
df['End Day'].fillna(2, inplace=True)
df = df.dropna(subset="End Month")
df = df.dropna(subset="Start Month")

df['Start Month'] = df['Start Month'].astype(int)
df['Start Day'] = df['Start Day'].astype(int)
df['End Month'] = df['End Month'].astype(int)
df['End Day'] = df['End Day'].astype(int)

df['start_date'] = df['Start Year'].astype(str) + '-' + df['Start Month'].astype(str) + '-' + df['Start Day'].astype(
    str)
df['end_date'] = df['End Year'].astype(str) + '-' + df['End Month'].astype(str) + '-' + df['End Day'].astype(str)
df.drop(df[df["end_date"] == "2017-6-31"].index, inplace=True)
df.drop(df[df["end_date"] == "1992-9-31"].index, inplace=True)

df['end_date'] = pd.to_datetime(df['end_date'])
df['start_date'] = pd.to_datetime(df['start_date'])
df["duration"] = df["end_date"] - df["start_date"]

df["duration"] = df["duration"].dt.days
print(df["duration"])

df.to_csv('meteo2.csv', index=False)

"""## ETS: Serie de tiempo"""

df.columns

df.head()

df['Month'] = df['Start Month']

# Convertir las columnas Month y Year a tipo string
df['Month'] = df['Month'].astype(str)
df['Year'] = df['Year'].astype(str)

# Concatenar las columnas Month y Year con un separador
df['year_month'] = df['Year'] + '-' + df['Month']

df.columns

# Agrupar por año y calcular el total
df_gr = df.groupby(['year_month']).size().reset_index(name='total')
df_gr

from sklearn.model_selection import train_test_split

X = df_gr[['total']]
y = df_gr['year_month']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Por mes y continnete

import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error

# Agrupar por año y calcular el total
grouped_data = df.groupby(['year_month']).size().reset_index(name='total')

# Verificar si hay suficientes datos para el análisis
if len(grouped_data) >= 2:
    # Conjunto de entrenamiento y prueba
    train = grouped_data.loc[:len(grouped_data) - 2, 'total']
    test = grouped_data.loc[len(grouped_data) - 1:, 'total']

    # Modelo ETS (Exponential Smoothing)
    model = ExponentialSmoothing(train)
    forecast = model.fit().forecast(steps=12)

    # Calcular la precisión del modelo manualmente
    accuracy = abs(test.values - forecast[:len(test)])
    mean_absolute_error = accuracy.mean()

    # Imprimir la precisión del modelo
    print("Precisión del modelo: ", mean_absolute_error)
else:
    print("No hay suficientes datos para el análisis")

len

grouped_data

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt


def forecast_disaster(disaster):
    # Filtrar por tipo de desastre
    filtered_data = df[df['Disaster Type'] == disaster]

    # Agrupar por año y calcular el total
    grouped_data = filtered_data.groupby(['Year', 'Month']).size().reset_index(name='total')

    # Crear la serie de tiempo
    serie = pd.Series(grouped_data['total'])

    # Ajustar el modelo ARIMA
    model = ARIMA(serie, order=(1, 0, 0))
    model_fit = model.fit()

    # Realizar la predicción
    forecast = model_fit.forecast(steps=10)

    # Graficar la serie y la predicción
    plt.plot(serie, label='Actual')
    plt.plot(forecast, label='Forecast')
    plt.legend()
    plt.show()

    # Generar las fechas para la predicción
    year = range(2022, 2032)
    df_pred = pd.DataFrame({'year': year})

    # Realizar la predicción con intervalo de confianza
    prediction = model_fit.get_forecast(steps=10)
    forecast_values = prediction.predicted_mean
    forecast_ci = prediction.conf_int()

    # Imprimir los resultados
    print("Forecasting", disaster)
    result = pd.concat([df_pred, forecast_values, forecast_ci], axis=1)
    result.columns = ['year', 'forecast', 'lower_ci', 'upper_ci']
    print(result)


# Ejemplo de uso
forecast_disaster("Flood")

"""## Otro

en este apis el ulitmo fue hasce dos años y el anteroiro hace tanto,.... calcua rdiferneica entre la ultima vez y al siguiente
"""

df.columns

dfa = df[df.Country == 'Argentina']
dfa['Disaster Subtype 2.0'].value_counts()

dfa = dfa[dfa['Disaster Subtype 2.0'] == 'Riverine flood']

from datetime import datetime, timedelta

fecha_prevista = dfa["start_date"].max() + timedelta(days=10)
print(fecha_prevista.date())

dfa_sorted = dfa['start_date'].sort_values(ascending=True)

# Calcular la dinámica entre fechas
dynamics = dfa_sorted.diff().dt.days

df2 = pd.DataFrame({'Dinámica': dynamics})
df2.reset_index(drop=True, inplace=True)

df2.dropna(inplace=True)
df2

# Crear un objeto de alisado exponencial y ajustarlo a los datos
modelo = ExponentialSmoothing(df2['Dinámica'], trend='additive', seasonal=None)
ajuste = modelo.fit()

# Predecir la próxima distancia temporal
proxima_distancia = ajuste.forecast(1)

# Imprimir la predicción
print(f"La próxima distancia temporal será aproximadamente {round(proxima_distancia.iloc[0])} dias.")

type

from datetime import datetime, timedelta

fecha_prevista = dfa["start_date"].max() + timedelta(days=round(proxima_distancia.iloc[0]))
print(fecha_prevista.date())

proxima_distancia.iloc[0]

# Crear un objeto de alisado exponencial y ajustarlo a los datos
modelo = ExponentialSmoothing(df2, trend='additive', seasonal=None)
ajuste = modelo.fit()

# Predecir la próxima distancia temporal
proxima_distancia = ajuste.forecast(1)



import warnings


def diferencia_fechas(pais, desastre):
    dfa = df[df.Country == pais]
    dfa = dfa[dfa['Disaster Subtype 2.0'] == desastre]

    dfa_sorted = dfa['start_date'].sort_values(ascending=True)

    # Calcular la dinámica entre fechas
    dynamics = dfa_sorted.diff().dt.days

    df2 = pd.DataFrame({'Dinámica': dynamics})
    df2.reset_index(drop=True, inplace=True)
    df2.dropna(inplace=True)

    # Crear un objeto de alisado exponencial y ajustarlo a los datos
    warnings.filterwarnings('ignore')
    modelo = ExponentialSmoothing(df2['Dinámica'], trend='additive', seasonal=None)
    ajuste = modelo.fit()

    # Predecir la próxima distancia temporal
    proxima_distancia = ajuste.forecast(1)

    fecha_prevista = dfa["start_date"].max() + timedelta(days=round(proxima_distancia.iloc[0]))
    return fecha_prevista.date()

    # Imprimir la predicción
    # print(f"El proximo será aproximadamente {round(proxima_distancia.iloc[0])} dias.")

    # Mostrar el DataFrame resultante

    # df2.dropna(inplace=True)
    # df2.plot(kind='line')
    # plt.xlabel('Eventos')
    # plt.ylabel('Distancia entre fechas')
    # plt.title('Dinámica entre fechas a lo largo del tiempo')
    # plt.show()


df['Disaster Subtype 2.0'].value_counts()

diferencia_fechas('Chile', 'Riverine flood')

diferencia_fechas("Argentina", 'Riverine flood')