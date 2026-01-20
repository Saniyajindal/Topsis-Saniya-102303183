import sys
import pandas as pd
import numpy as np


def topsis(input_file, weights, impacts, output_file):
    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        raise Exception("Input file must have at least 3 columns")

    matrix = data.iloc[:, 1:].values.astype(float)

    if len(weights) != matrix.shape[1]:
        raise Exception("Number of weights must match number of criteria")

    if len(impacts) != matrix.shape[1]:
        raise Exception("Number of impacts must match number of criteria")

    # Step 1: Normalization
    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # Step 2: Weighting
    weighted_matrix = norm_matrix * weights

    # Step 3: Ideal Best & Worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix[:, i].max())
            ideal_worst.append(weighted_matrix[:, i].min())
        elif impacts[i] == '-':
            ideal_best.append(weighted_matrix[:, i].min())
            ideal_worst.append(weighted_matrix[:, i].max())
        else:
            raise Exception("Impacts must be + or -")

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance Calculation
    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: TOPSIS Score
    score = dist_worst / (dist_best + dist_worst)

    rank = score.argsort()[::-1].argsort() + 1

    data["Topsis Score"] = score
    data["Rank"] = rank

    data.to_csv(output_file, index=False)


def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(",")))
    impacts = sys.argv[3].split(",")
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
