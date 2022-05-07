from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import datetime as dt
import statsmodels.api as sm


df_limpio = pd.read_csv(".././PollutionSK/csv/south-korean-pollution-data_limpio.csv", index_col= "Unnamed: 0")
df_limpio['date']= pd.to_datetime(df_limpio['date'], format ="%d-%m-%Y")
df_limpio[' co'] = pd.to_numeric(df_limpio[' co'], errors='coerce')
df_co = df_limpio.groupby([df_limpio["date"].dt.year, df_limpio["date"].dt.month, df_limpio["City"]]).agg({" co": ['min', 'max', 'mean']})
df_co.index = df_co.index.set_names(['year', 'month', 'city'])
df_co = df_co.reset_index() 


df_bm = pd.DataFrame(data=df_co['year'])
df_bm = df_bm.assign(month=df_co['month'])
df_bm = df_bm.assign(city=df_co['city'])
df_bm = df_bm.assign(co_mean=df_co[' co']['mean'])

df_bm["date"] = df_co["month"].map(str) + "-" + df_co["year"].map(str)
df_bm["date_num"] = pd.to_datetime(df_bm['date'], format ="%m-%Y")
df_bm["date_num"] = df_bm["date_num"].map(dt.datetime.toordinal)
df_bm0 = df_bm[df_bm["city"] == "Bangsan-Myeon"]


X = (df_bm0.iloc[:,5].values - 735234)
y = df_bm0.iloc[:,3].values
X0 = sm.add_constant(X)
mod = sm.OLS(y, X0)
res = mod.fit()
print(res.summary())

coef = pd.read_html(res.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
predicciones0 = (coef.values[0] +  coef.values[1] * X)
bounds = res.conf_int(0.05)

ci_low = bounds[0][0]  + coef.values[1] * X
ci_up = bounds[0][1] + coef.values[1] * X

plt.figure(figsize=(22,10))
plt.plot(X, y, "o")
plt.plot(X, predicciones0, "-",  color='red')
plt.fill_between(df_bm0.iloc[:,5].values - 735234, ci_low, ci_up, alpha = 0.2, color = "green")
plt.xlabel("Fechas")
plt.xticks(df_bm0["date_num"].values - 735234, df_bm0["date"].values, rotation = 90)
plt.savefig('.././PollutionSK/imgs/regresion_lineal_forecasting/Forecasting_co_Bangsan-Myeon.jpg')
