from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "this is my first program"
###____INT___
# @app.route('/<int:date>')
# def hellod(date):
#     return "date = %d" % date

###___Floot___
@app.route('/<float:date>')
def hellod(date):
    return "date = %f" % date

###___Name URL___
# @app.route('/<name>')
# def helloname(name):
#     return "Hello "+ name
app.run(debug=True)