
from flask import Flask

app = Flask(__name__)

@app.route("/kase_ho")
def home():
    return "Hello, this is my first Flask server!"

if __name__ == "__main__":
    app.run(debug=True)