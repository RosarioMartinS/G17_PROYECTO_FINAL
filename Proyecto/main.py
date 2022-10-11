from flask import Flask, flash, request, redirect, url_for, render_template, session
import os # The OS module in Python provides functions for creating and removing a directory (folder),
# fetching its contents, changing and identifying the current directory, etc.

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
        return redirect('/register')

app.run(host='0.0.0.0', port=81)