from statsmodels.stats.weightstats import ztest as ztest
import pandas as pd
from scipy.stats import shapiro
import pingouin as pg
import numpy as np



df_limpio = pd.read_csv(".././PollutionSK/csv/south-korean-pollution-data_limpio.csv", index_col= "Unnamed: 0")


df_limpio[' no2'] = pd.to_numeric(df_limpio[' no2'], errors='coerce')
df_limpio[' o3'] = pd.to_numeric(df_limpio[' o3'], errors='coerce')

df_limpio = df_limpio.fillna(0)

#Comparar promedios 
#Prueba de diferencia de medias

prueba = ztest(df_limpio[" o3"], df_limpio[" no2"])
print("\n\n --Prueba del estadistico z para verificar la diferencia de medias.")
print("El valor p es: ", prueba[1])
print ("El estadistico de prueba z, es: ", prueba[0])
print ("Entonces:" , prueba[0], "> 2.5")
print ("Como el valor critico es 2.5, se rechaza h0, por lo tanto, se concluye que las medias de ambos gases son significativamente diferentes.\n")



#Prueba para verificar si los datos son normales

stat,p = shapiro(np.log(df_limpio[" o3"] +.1))
print("\n\n --Para verificar si los datos tienen una distribución normal, realizamos la prueba de Shapiro-Wilk")
print("El valor p es: ", p)
print("Como podemos ver, el valor de p es nulo, por lo tanto, se dice que los datos no son normales, así que la prueba realizada anteriormente, pierde veracidad.")



#Prueba Mann-Whitney-Wilcoxon (Prueba no parametrica)

df_muestra = df_limpio.sample(1000)
pnm = pg.mwu(df_muestra[" o3"], df_muestra[" no2"])
print("\n\n --Prueba no parametrica Mann-Whitney-Wilcoxon:")
print("El valor de p es: ", pnm.iloc[0]['p-val'])
print ("El valor de u es: ", pnm.iloc[0]["U-val"])
print("Como", pnm.iloc[0]['p-val'], "< 0.05, entonces, podemos concluir que las medianas son diferentes.")


