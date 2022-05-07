from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
from tabulate import tabulate
import datetime as dt
import statsmodels.api as sm


#Leemos y acomodamos los datos para realizar la regresión lineal

df_limpio = pd.read_csv(".././PollutionSK/csv/south-korean-pollution-data_limpio.csv", index_col= "Unnamed: 0")
df_limpio['date']= pd.to_datetime(df_limpio['date'], format ="%d-%m-%Y")
df_limpio[' co'] = pd.to_numeric(df_limpio[' co'], errors='coerce')
df_co = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" co": ['min', 'max', 'mean']})
df_co.index = df_co.index.set_names(['year', 'month', 'city'])
df_co = df_co.reset_index() 

#print(df_co[(' co', 'mean')])
#print(df_co[' co']['mean'])

df_bm = pd.DataFrame(data=df_co['year'])
df_bm = df_bm.assign(month=df_co['month'])
df_bm = df_bm.assign(city=df_co['city'])
df_bm = df_bm.assign(co_mean=df_co[' co']['mean'])

df_bm["date"] = df_co["month"].map(str) + "-" + df_co["year"].map(str)
df_bm["date_num"] = pd.to_datetime(df_bm['date'], format ="%m-%Y")
df_bm["date_num"] = df_bm["date_num"].map(dt.datetime.toordinal)
df_bm0 = df_bm[df_bm["city"] == "Bangsan-Myeon"]

#Empezamos a realizar la regresión lineal

X = (df_bm0.iloc[:,5].values - 735234).reshape(-1,1)
y = df_bm0.iloc[:,3].values

reg = LinearRegression().fit(X, y)
predicciones = reg.predict(X)

plt.figure(figsize=(22,10))
plt.plot(X, y, "o")
plt.plot(X, predicciones, "-",  color='red')
plt.xlabel("Fechas")
plt.ylabel("Promedio_co")
plt.xticks(df_bm0["date_num"].values - 735234, df_bm0["date"].values, rotation = 90)
print("La regresión lineal para los promedios de co de la ciudad de Bangsan-Myeon es:")
#plt.show()
plt.savefig('.././PollutionSK/imgs/regresion_lineal_forecasting/regresion_lineal_co_Bangsan-Myeon.jpg')
plt.close('all')
b = reg.intercept_
m = reg.coef_
print("La ordenada al origen es:", b)
print("La pendiente es:", m)
