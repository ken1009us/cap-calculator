from flask import Flask, request, jsonify, render_template
from calculator import calculation

# Create the app object
app = Flask(
    __name__,
    template_folder="./templates/",
    static_folder="./static/",
    # template_folder="/home/ken1009/mysite/templates/",
    # static_folder="/home/ken1009/mysite/static/",
)


# Define calculator
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    sprintDays = request.form["a"]
    hoursPerDay = request.form["b"]
    meetingHours = request.form["c"]
    ptoHours = request.form["d"]

    res = calculation(sprintDays, hoursPerDay, meetingHours, ptoHours)

    return render_template("index.html", prediction_text=res)


if __name__ == "__main__":
    app.run()
