import pandas as pd
import numpy as np

def run_topsis(input_file, weights, impacts):
    data = pd.read_excel(input_file) if input_file.endswith(".xlsx") else pd.read_csv(input_file)

    alternatives = data.iloc[:, 0]
    matrix = data.iloc[:, 1:].values.astype(float)

    weights = np.array(weights)

    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted_matrix = norm_matrix * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix[:, i].max())
            ideal_worst.append(weighted_matrix[:, i].min())
        else:
            ideal_best.append(weighted_matrix[:, i].min())
            ideal_worst.append(weighted_matrix[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    rank = score.argsort()[::-1].argsort() + 1

    data["Topsis Score"] = score
    data["Rank"] = rank

    return data

