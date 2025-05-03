from flask import Flask, render_template, request, redirect, url_for
from livereload import Server

app = Flask(__name__)


"""login pag"""
@app.route('/')
def index():
    return render_template('login.html')

"""Check uesername and password"""
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'Jetsada' and password == 'pizza1112':
        return redirect(url_for('dashboard'))
    else:
        return "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"
    

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')




if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('static/*.*')          # ตรวจจับไฟล์ใน static/
    server.watch('templates/*.*l')    # ตรวจจับ HTML
    server.watch('app.py')

    server.serve()