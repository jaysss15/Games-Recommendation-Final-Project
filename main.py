from flask import Flask, render_template, request
import pandas
from sklearn.tree import DecisionTreeClassifie

data = pandas.read_csv("games.csv")
x = data.drop(columns=["games"])
y = data["games"]
model = DecisionTreeClassifier()
model.fit(x.values ,y)


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def home():
    action = 0
    strategy = 0
    fantasy = 0
    adventure = 0

    if request.method == "POST":
        Aaction = request.form["action"]
        Sstrategy = request.form["strategy"]
        Ffantasy = request.form["fantasy"]
        Aadventure = request.form["adventure"]

        action = Aaction
        strategy = Sstrategy
        fantasy = Ffantasy
        adventure = Aadventure

    predicted_value = model.predict([[action, strategy, fantasy, adventure]])

    return render_template("index.html" ,firstname=predicted_value[0])


if __name__ == "__main__":
    app.run(debug=True)
