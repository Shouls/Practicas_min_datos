from array import array
from tokenize import group
import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime
import os

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def rellenar_celda_vacia(celda_txt: str) -> str:
    celda_txt = celda_txt.replace("", "NA")
    return celda_txt

def cambiar_fecha(fecha_txt: str) -> str:
    return str (fecha_txt.replace("/", "-"))


#AAAA-MM-DD
def inv_fecha(gfecha_txt: str) -> str:

    anio = gfecha_txt[:4]

    mes_dia = gfecha_txt[5:]

    find = mes_dia.find('-')
    mes = mes_dia[:find]
 
    dia = mes_dia[(find+1):]

    if(int(mes) < 10):
        mes = "0" + mes
    
    if(int(dia) < 10):
        dia = "0" + dia

    fecha_conv = dia + "-" + mes + "-" + anio
    #print(fecha_conv)
    #os.system("pause")
    return str(fecha_conv)

#leemos datos obtenidos en P1
df = pd.read_csv("south-korean-pollution-data.csv")


#cambiar fecha Formato // por --
df['date'] = df['date'].transform(cambiar_fecha)
df['date'] = df['date'].transform(inv_fecha)

#guardamos cambios
print_tabulate(df)
df.to_csv(".././PollutionSK/csv/south-korean-pollution-data_limpio.csv", index=False) 
# Verificamos  
# abr = pd.read_csv(".././Practicas/DATA_limpio.csv", low_memory = False)
# print_tabulate(abr)









