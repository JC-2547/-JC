from flask import Flask, render_template, request
from livereload import Server

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "Jetsada" and password == "pizz1112":
        return "Login Success"
    else:
        return "Login Fail"


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('templates/*.*')
    server.watch('static/*.*')
    server.watch('app.py')
    server.serve()