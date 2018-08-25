# Michael Spearing
# August 23, 2018

from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return('Hello, World!')

@app.route('/michael/')
def hello_michael():
    return('Hello, Michael!')

# <variable_name> allows for passing of variables to the URL
@app.route('/user/<username>')
def show_user_profile(username):
    #Show the user profile for the given user
    return('User: %s' % username)

# <converter:variable_name> allows for specifying the type of variable
# Can be: string, int, float, path, uuid
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Show the post with the given id, the id must be an integer
    return('Post %d' % post_id)

with app.test_request_context():
    # Use url_for to create URLs based off of functions - avoids hard coding
    print(url_for('hello_michael'))
    print(url_for('show_user_profile', username='MS48571'))
    print(url_for('show_post', post_id=12345))

# By default, a FLASK route only handles GET requests. Can specify others
@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method== 'POST':
            return(do_the_login())
        else:
            return(show_the_login_form())

def do_the_login():
    return("Logged in!")

def show_the_login_form():
    return("Return to login?")

# Static files can be held in the "static" folder and referenced with the keyword below
with app.test_request_context():
    print(url_for('static', filename='style.css'))

# Rendering Templates - Based off of HTML formatting
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('Architect.html', name=name)