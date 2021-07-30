# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
# from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return "hello world"

@app.route('/graduation')
def graduation():
    return "<h1>HAPPY GRADUATION!</h1>"
