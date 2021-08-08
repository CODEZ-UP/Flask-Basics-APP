from flask import Flask, jsonify, request, render_template;

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(['Welcome to Codez Up'])


@app.route("/about/")
def about():
    return "This is About Page of Codez Up"

@app.route("/employee/<string:eName>")
def EmployeeName(eName):
    return "Employee Name : %s" %eName

@app.route("/cube/<int:number>")
def cubeofNumber(number):
    return "Cube of %d = %d" %(number, number**3)

@app.route("/login/" , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login Page"
    else:
        return "Register Page"

@app.route("/welcome/")
@app.route("/welcome/<string:name>")
def template(name=None):
    return render_template("codezup.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)

