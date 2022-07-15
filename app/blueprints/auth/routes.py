from flask import render_template, request
from . import bp as app
from app.blueprints.main.models import User
from app import db

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            email = request.form['emailInput'],
            password = request.form['passwordInput'],
            username=request.form['usernameInput'],
            first_name= request.form['first_nameInput'],
            last_name = request.form['last_nameInput']
        )
        db.session.add(new_user)
        db.session.commit()
        return request.form
    else:
        return render_template("register.html")