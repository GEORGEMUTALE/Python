from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students")
def students():
    student_list = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"]
    return render_template("students.html", students=student_list)

if __name__ == "__main__":
    app.run(debug=True)
