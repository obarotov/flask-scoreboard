from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("/main_page.html")

@app.route("/about")
def about():
    return render_template("/about.html")



@app.route('/students')
def students():
 students_data = {
    "Abdul-Aziz": 77, "Abdullo": 47, "Abubakr": 59,
    "Ahmadjon": 69, "Amir": 44, "Behruz": 69,
    "Habibulloh": 51, "Ilyos": 64, "Maftunbek": 39,
    "Maryam": 28, "Mubarro": 22, "Najmiya": 60,
    "Otabek": 48, "Shahrom": 83, "Habibullo": 63,
    "Rukhshona": 31, "Osiya": 69, "Bakhtiyor": 32,
    "Muhammadjon": 0, "Timur": 89, "Gulsum": 36,
    "Rayhona": 39, "Abduvozit": 12, "Ismoiljon": 0,
    "Nizar": 72,
}
 sorted_students = sorted(students_data.items(), key=lambda x: x[1], reverse=True)

 return render_template('students.html', students=sorted_students)

@app.route("/student/<name>")
def student_detail(name):
    search_name = name.title() 

    students_data = {
        "Abdul-Aziz": 77, "Abdullo": 47, "Abubakr": 59,
        "Ahmadjon": 69, "Amir": 44, "Behruz": 69,
        "Habibulloh": 51, "Ilyos": 64, "Maftunbek": 39,
        "Maryam": 28, "Mubarro": 22, "Najmiya": 60,
        "Otabek": 48, "Shahrom": 83, "Habibullo": 63,
        "Rukhshona": 31, "Osiya": 69, "Bakhtiyor": 32,
        "Muhammadjon": 0, "Timur": 89, "Gulsum": 36,
        "Rayhona": 39, "Abduvozit": 12, "Ismoiljon": 0,
        "Nizar": 72,
    }

    if search_name not in students_data:
        return render_template("/404.html")
    
    score = students_data[search_name]
    
    if score >= 80:
        result = 'Excellent'
    elif 50 <= score <= 79:
        result = "Good"
    elif 1 <= score <= 49:
        result = "Needs improvement"
    else:
        result = "No data"
    
    return render_template("student.html", name=search_name, score=score, result=result)


if __name__ == "__main__":
    app.run(debug=True)