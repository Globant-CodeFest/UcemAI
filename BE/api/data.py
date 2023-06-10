import pandas as pd

def obtener_columna_como_array(ruta_archivo, value):
    df = pd.read_csv(ruta_archivo)
    df_country = df[df['Country'] == value]

    natural_disasters = df_country['Disaster Subtype 2.0'].to_numpy()

    count_nd = list()

    for i in natural_disasters:
        df_new = df_country[df_country['Disaster Subtype 2.0'] == i]
        count_nd.append(len(df_new))

    return {"natural_disasters": natural_disasters.tolist(), "count_nd": count_nd}
