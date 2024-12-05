from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/calc", methods=["POST"])
def calc():
    height=request.form["height"]
    weight=request.form["weight"]
    bmi=int(weight) / (int(height) / 100) ** 2
    message = "あなたのBMIは" + str(bmi) + "です。"
    return render_template("index.html",height = height, weight = weight, message = message)