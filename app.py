from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    navn = "Higher or Lower"
    return render_template("index.html", navn=navn)

app.run(debug=True)