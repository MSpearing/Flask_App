# Michael Spearing
# August 23, 2018

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return('Hello, World!')

@app.route('/michael/')
def hello_michael():
    return('Hello, Michael!')