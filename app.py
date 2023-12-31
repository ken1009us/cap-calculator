from flask import Flask, request, jsonify, render_template
from calculator import calculate_capacity


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
    """
    Render the homepage with the capacity calculator form.
    """
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    """
    Handle the capacity calculation request and display the result.
    """
    sprint_days = request.form["sprint_days"]
    hours_per_day = request.form["hours_per_day"]
    meeting_hours = request.form["meeting_hours"]
    pto_hours = request.form["pto_hours"]

    result = calculate_capacity(sprint_days, hours_per_day, meeting_hours, pto_hours)
    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run()
