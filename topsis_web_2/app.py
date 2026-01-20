from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "TOPSIS WEB WORKING"

if __name__ == "__main__":
    print("SERVER STARTING...")
    app.run(debug=True)
