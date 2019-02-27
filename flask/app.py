from flask import Flask, abort, make_response, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello(name):
    return 'Hello, ' + name


@app.route('/id/<int:id>')
def user_id(id):
    return 'Your ID is {}'.format(id)


@app.route('/url/<route_name>')
def build_url(route_name):
    try:
        return url_for(route_name)
    except Exception as e:
        return 'Build failed: {}'.format(e)


@app.route('/method/get', methods=['GET'])
def only_get():
    return 'GET'


@app.route('/method/post', methods=['POST'])
def only_post():
    return 'POST'


@app.route('/example.xml')
def static_file():
    return url_for('static', filename='example.xml')


@app.route('/template/<name>')
def rendering_template(name):
    return render_template('hello.html', name=name)


@app.route('/data')
def accessing_request_data():
    return 'path: {}, query: {}, a: {}'.format(request.path, request.query_string, request.args.get('a'))


@app.route('/cookie')
def setting_cookie():
    response = make_response(render_template('hello.html'))
    response.set_cookie('username', 'test')
    return response


@app.route('/redirect')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/unauthorized')
def unauthorized():
    abort(401)


@app.errorhandler(401)
def access_denied(error):
    return '<p>You shall not pass!</p><p>{}</p>'.format(error)
