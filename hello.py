from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/sitemap', methods=['GET'])
def sitemap():
    return url_for('hello_world')
