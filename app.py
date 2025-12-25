from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/restaurant")
def restaurant():
    return render_template("restaurant.html")

@app.route("/resort")
def resort():
    return render_template("resort.html")

if __name__ == "__main__":
    app.run(debug=True)
