from flask import Blueprint, render_template, request, flash
from todolist.models import User
from todolist import db
from werkzeug.security import generate_password_hash

user = Blueprint("user", __name__)

@user.route("/login")
def login():
    return render_template("login.html")


@user.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        user_name = request.form.get("user_name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash("User existed", category="error")
        elif len(email) < 4:
            flash("Email too short", category="error")
        elif len(password) < 7:
            flash("Password to short", category= "error")
        elif password != confirm_password:
            flash("Password do not match", category= "error")
        else:
            try:
                new_user = User(email=email, password=generate_password_hash(password=password, method="sha256"), user_name=user_name)
                db.session.add(new_user)
                db.session.commit()
                flash("User created", category="success")
            except:
                flash("User created error", category= "error")

    return render_template("signup.html")


@user.route("/logout")
def logout():
    return "logout page"