import pandas as pd
import matplotlib.pyplot as plt
from typing import List
import numpy as np

def k_means(points: List[np.array], k: int):
    DIM = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 1

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, DIM))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0)
        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred
            
    plt.figure(figsize = (15,10))
    plt.title("K_means")
    plt.xlabel("valor de o3")
    plt.ylabel("valor de no2")
    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 1]
        plt.scatter(xp, yp)
    plt.savefig(".././PollutionSK/imgs/clasifi_clust/k_means.jpg")
    plt.close()
    return mean



df_limpio = pd.read_csv(".././PollutionSK/csv/south-korean-pollution-data_limpio.csv", index_col= "Unnamed: 0")
df_limpio['date']= pd.to_datetime(df_limpio['date'], format ="%d-%m-%Y")
df_limpio[' o3'] = pd.to_numeric(df_limpio[' o3'], errors='coerce')
df_limpio[' no2'] = pd.to_numeric(df_limpio[' no2'], errors='coerce')
df_2 = df_limpio[['date', ' o3', ' no2']]
df_2['label'] =  [str(fecha.month) for fecha in df_limpio['date']]
df_2 = df_2.drop('date', axis=1)
df_2 = df_2.dropna()

list_t = [
    (np.array(tuples[0:2]), tuples[2])
    for tuples in df_2.itertuples(index=False, name=None)
]

points = [point for point, _ in list_t]

k_m = k_means(points, 8)


