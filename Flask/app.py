from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "this is my first program"
@app.route('/raj')
def Hello_RAj():
    return "Hello Raj Kumar"
app.run(debug=True)