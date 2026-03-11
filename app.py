from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("/main_page.html")

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route("/student/<name>")
def student(name):
    return f"Hello {name}"


@app.route("/grade/<name>/<int:score>")
def grade(name,score):
    if score >= 80:
        result = "Excellent"
    elif score >= 50:
        result = "Good"
    else:
        result = "Needs practice"
    return f"{name}: {score}% - {result}"



if __name__ == "__main__":
    app.run(debug=True)