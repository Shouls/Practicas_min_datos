import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))


def analisis_graficar(nombre_archivo:str)->None:

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
    df_co = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" co": ['min', 'max', 'mean']})   #[[" co"]].aggregate(pd.DataFrame.sum)

    #GRAFICAR (Practica0_4)

    #Guardamos las graficas para cada particula


    #graficas pm25

    imgs_pm25 = df_pm25.groupby("City").plot(kind = 'bar', figsize=(32,18))
    for i in range(20):
        g25 = imgs_pm25[i].get_figure()
        g25.savefig('.././PollutionSK/imgs/pm25/pm25_ciudad{0:3d}.jpg'.format(i))
        plt.close('all')

    #graficas pm10
    imgs_pm10 = df_pm10.groupby("City").plot(kind = 'bar', figsize=(32,18))
    for i in range(20):
        g10 = imgs_pm10[i].get_figure()
        g10.savefig('.././PollutionSK/imgs/pm10/pm10_ciudad{0:3d}.jpg'.format(i))
        plt.close('all')

    #graficas o3
    imgs_o3 = df_o3.groupby("City").plot(kind = 'bar', figsize=(32,18))
    for i in range(20):
        go3 = imgs_o3[i].get_figure()
        go3.savefig('.././PollutionSK/imgs/o3/o3_ciudad{0:3d}.jpg'.format(i))
        plt.close('all')

    #graficas no2
    imgs_no2 = df_no2.groupby("City").plot(kind = 'bar', figsize=(32,18))
    for i in range(20):
        gno2 = imgs_no2[i].get_figure()
        gno2.savefig('.././PollutionSK/imgs/no2/no2_ciudad{0:3d}.jpg'.format(i))
        plt.close('all')

    #graficas so2
    imgs_so2 = df_so2.groupby("City").plot(kind = 'bar', figsize=(32,18))
    for i in range(20):
        gso2 = imgs_so2[i].get_figure()
        gso2.savefig('.././PollutionSK/imgs/so2/so2_ciudad{0:3d}.jpg'.format(i))
        plt.close('all')

    #graficas co
    imgs_co = df_co.groupby("City").plot(kind = 'bar', figsize=(32,18))
    for i in range(20):
        gco = imgs_co[i].get_figure()
        gco.savefig('.././PollutionSK/imgs/co/co_ciudad{0:3d}.jpg'.format(i))
        plt.close('all')

    
    #Se guardan los diferentes csv con el analisis realizado
    df_pm25.to_csv(".././PollutionSK/csv/pm25.csv")
    df_pm10.to_csv(".././PollutionSK/csv/pm10.csv")
    df_o3.to_csv(".././PollutionSK/csv/o3.csv")
    df_no2.to_csv(".././PollutionSK/csv/no2.csv")
    df_so2.to_csv(".././PollutionSK/csv/so2.csv")
    df_co.to_csv(".././PollutionSK/csv/co.csv")


analisis_graficar(".././PollutionSK/csv/south-korean-pollution-data_limpio.csv")




