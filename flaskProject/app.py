from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/about')
def about():
    return "Hello about"


@app.route('/')
def home():
    return redirect('/about')

@app.route('/redi')
def hello_world():
    return redirect(url_for('/about'))



