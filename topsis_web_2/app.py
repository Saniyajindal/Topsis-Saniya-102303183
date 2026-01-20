from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "topsis_web/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def run_topsis(input_file, weights, impacts):
    data = pd.read_excel(input_file) if input_file.endswith(".xlsx") else pd.read_csv(input_file)

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = list(map(float, request.form["weights"].split(",")))
        impacts = request.form["impacts"].split(",")

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        result = run_topsis(filepath, weights, impacts)
        result_path = os.path.join(UPLOAD_FOLDER, "result.csv")
        result.to_csv(result_path, index=False)

        return send_file(result_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
