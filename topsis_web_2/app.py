from flask import Flask, render_template, request
import os
from topsis import run_topsis

app = Flask(__name__)

UPLOAD_FOLDER = "topsis_web/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["file"]
        weights = list(map(float, request.form["weights"].split(",")))
        impacts = request.form["impacts"].split(",")

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        result = run_topsis(file_path, weights, impacts)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

