from flask import Flask, flash, request, redirect, url_for, render_template, session
import os # The OS module in Python provides functions for creating and removing a directory (folder),
# fetching its contents, changing and identifying the current directory, etc.
import sqlite3

from werkzeug.utils import secure_filename
UPLOAD_FOLDER = './static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
path = './static/img'
path2 = 'img'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "asdasdazsdawefdfascacs"

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def registro():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        session['usuario'] = request.form["username"]
        session['contraseña'] = request.form["user-password"]
        session['mail'] = request.form['e-mail']
        session['nombre'] = request.form['name']
        session['mail'] = session['mail'].replace("@", ".")

        print(session['mail'])

        return redirect('/añadirUsuario')

@app.route('/añadirUsuario', methods=['POST', 'GET'])
def agregarUsuario():
    if request.method == "POST":
        conn = sqlite3.connect('SocialMedia.db')
        q = f"""INSERT INTO Usuarios(nombre, contraseña, mail, username) 
                VALUES('{session['nombre']}', '{session['contraseña']}', '{session['mail']}', '{session['usuario']}')"""
        conn.execute(q)
        conn.commit()
        conn.close()
        return render_template("base.html")
    elif request.method == "GET":
        return redirect('/register')

app.run(host='0.0.0.0', port=81)