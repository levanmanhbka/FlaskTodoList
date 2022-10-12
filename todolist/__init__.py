from flask import Flask
import os
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
DB_NAME = os.environ.get("DB_NAME")
# print(SECRET_KEY)
# print(DB_NAME)

def create_database(app):
    if not os.path.exists("todolist/" + DB_NAME):
        db.create_all(app= app)

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["DB_NAME"] = DB_NAME
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app=app)
    
    from todolist.models import Note, User
    create_database(app=app)

    from todolist.user import user
    from todolist.views import views
    
    app.register_blueprint(user)
    app.register_blueprint(views)
    return app