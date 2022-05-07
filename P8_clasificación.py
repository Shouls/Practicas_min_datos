import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from typing import List
import numpy as np
from scipy.stats import mode


    
def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)

def scatter_group_by(archivo: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str):
    fig, ax = plt.subplots(figsize=(10, 8))
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i), linewidths = 0.2)
    ax.legend()
    plt.xlabel("Valor de o3")
    plt.ylabel("Valor de no2")
    plt.savefig(archivo)
    plt.close()


def distancia_eu(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))


def k_vecinos_mc(points: List[np.array], labels: np.array, input_data: List[np.array], k: int):
    input_distances = [
        [distancia_eu(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]


df_limpio = pd.read_csv(".././PollutionSK/csv/south-korean-pollution-data_limpio.csv", index_col= "Unnamed: 0")
df_limpio['date']= pd.to_datetime(df_limpio['date'], format ="%d-%m-%Y")
df_limpio[' o3'] = pd.to_numeric(df_limpio[' o3'], errors='coerce')
df_limpio[' no2'] = pd.to_numeric(df_limpio[' no2'], errors='coerce')
df_2 = df_limpio[['date', ' o3', ' no2']]
df_2['label'] =  [str(fecha.month) for fecha in df_limpio['date']]
df_2 = df_2.drop('date', axis=1)


list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df_2.itertuples(index=False, name=None)
]
puntos = [point for point, _ in list_t]
labels = [label for _, label in list_t]

k_vecinos_mc(puntos, labels, [np.array([15, 5]), np.array([3, 2]), np.array([1, 7]), np.array([2, 6])], 4)
scatter_group_by(".././PollutionSK/imgs/clasifi_clust/clasification_por_mes.jpg", df_2, " o3", " no2", "label")



