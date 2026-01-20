@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = list(map(float, request.form["weights"].split(",")))
        impacts = request.form["impacts"].split(",")

        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        result = run_topsis(file_path, weights, impacts)
        result.to_csv("uploads/result.csv", index=False)

        return send_file("uploads/result.csv", as_attachment=True)

    return render_template("index.html")
