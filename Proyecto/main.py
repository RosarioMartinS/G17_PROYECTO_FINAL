from flask import Flask, flash, request, redirect, url_for, render_template, session
import os # The OS module in Python provides functions for creating and removing a directory (folder),
# fetching its contents, changing and identifying the current directory, etc.
import sqlite3

from werkzeug.utils import secure_filename
from flask_socketio import SocketIO
UPLOAD_FOLDER = './static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
path = './static/img'
path2 = 'img'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "asdasdazsdawefdfascacs"
#socketio = SocketIO(app)

#if __name__ == '__main__':
#    socketio.run(app)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == "GET":
        return render_template("login.html", login = False)
    elif request.method == "POST":  
        return redirect('/')

@app.route('/usuarioIngresado', methods=['GET', 'POST'])
def checkearUsuario():
    if request.method == "GET":
        return redirect('/')
    elif request.method == "POST":
        session['contraseña'] = request.form["user-password"]
        session['usuario'] = request.form["username"]
        conn = sqlite3.connect('SocialMedia.db')
        q = f"""
                SELECT contraseña, username FROM Usuarios 
                WHERE contraseña = '{session['contraseña']}'
                and username = '{session['usuario']}'
                """
        resu = conn.execute(q)

        if resu.fetchone():
            return redirect('/home')
        else:
            flash('Usuario o contraseña incorrectos')
            return render_template("login.html", login = True)


@app.route('/register', methods=['GET', 'POST'])
def registro():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        return redirect('/')

@app.route('/añadirUsuario', methods=['POST', 'GET'])
def agregarUsuario():
    if request.method == "POST":
        session['usuario'] = request.form["username"]
        session['contraseña'] = request.form["user-password"]
        session['mail'] = request.form['e-mail']
        session["nombre"] = request.form['name']
        session['mail'] = session['mail'].replace("@", ".")

        conn = sqlite3.connect('SocialMedia.db')
        q = f"""INSERT INTO Usuarios(nombre, contraseña, mail, username) 
                VALUES('{session["nombre"]}', '{session['contraseña']}', '{session['mail']}', '{session['usuario']}')"""
        conn.execute(q)

        x = f"""CREATE TABLE IF NOT EXISTS {session['usuario']} 
            (publicacion TEXT);"""
        conn.execute(x)

        conn.commit()
        conn.close()
        return redirect('/')
    elif request.method == "GET":
        return redirect('/register')

@app.route('/home', methods=['POST','GET'])
def home():
    if request.method == "GET":
        return render_template("base.html")
    elif request.method == "POST":
        return redirect('/home')

@app.route('/profile', methods=['POST','GET'])
def profile():
    if request.method == "GET":
        return render_template("profile.html")
    elif request.method == "POST":
        return redirect('/home')



app.run(host='0.0.0.0', port=81)