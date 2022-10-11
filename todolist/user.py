from flask import Blueprint

user = Blueprint("user", __name__)

@user.route("/login")
def login():
    return "login page"


@user.route("/signup")
def signup():
    return "signup page"


@user.route("/logout")
def logout():
    return "logout page"