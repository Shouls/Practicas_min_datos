import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))


def analisis(nombre_archivo:str)->None:

    #Lee el csv
    df_limpio = pd.read_csv(nombre_archivo, index_col= "Unnamed: 0")

    #Convierte la columna date al tipo datetime
    df_limpio['date']= pd.to_datetime(df_limpio['date'], format = "%d-%m-%Y")

    #Convierte las columnas a numericos y evita que haya error con las filas vacías
    df_limpio[' pm25'] = pd.to_numeric(df_limpio[' pm25'], errors='coerce')
    df_limpio[' pm10'] = pd.to_numeric(df_limpio[' pm10'], errors='coerce')
    df_limpio[' o3'] = pd.to_numeric(df_limpio[' o3'], errors='coerce')
    df_limpio[' so2'] = pd.to_numeric(df_limpio[' so2'], errors='coerce')
    df_limpio[' no2'] = pd.to_numeric(df_limpio[' no2'], errors='coerce')
    df_limpio[' co'] = pd.to_numeric(df_limpio[' co'], errors='coerce')

    #Se realiza el analisis, por agrupación, sacamos min, max y promedio
    df_pm25 = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" pm25": ['min', 'max', 'mean']})
    df_pm10 = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" pm10": ['min', 'max', 'mean']}) 
    df_o3 = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" o3": ['min', 'max', 'mean']}) 
    df_no2 = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" no2": ['min', 'max', 'mean']}) 
    df_so2 = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" so2": ['min', 'max', 'mean']})
    df_co = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" co": ['min', 'max', 'mean']})

    df_pm25.to_csv(".././PollutionSK/csv/pm25.csv")
    df_pm10.to_csv(".././PollutionSK/csv/pm10.csv")
    df_o3.to_csv(".././PollutionSK/csv/o3.csv")
    df_no2.to_csv(".././PollutionSK/csv/no2.csv")
    df_so2.to_csv(".././PollutionSK/csv/so2.csv")
    df_co.to_csv(".././PollutionSK/csv/co.csv")

analisis(".././PollutionSK/csv/south-korean-pollution-data_limpio.csv")




