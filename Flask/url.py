from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Web Page"

@app.route('/student')
def student():
    return "Welcome student"

@app.route('/faculty')
def faculty():
    return "Welcome faculty"

@app.route('/user/<name>')
def user(name):
    if name=='student':
        return redirect(url_for('student'))
    if name=='faculty':
        return redirect(url_for('faculty'))
    
app.run(debug=True)