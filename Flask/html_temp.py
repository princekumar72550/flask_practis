from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# def hello():
#     return "<html><body><h4>this is my first program</h4></body></html>"
# @app.route('/raj')
# def Hello_RAj():
#     return "Hello Raj Kumar"
app.run(debug=True)