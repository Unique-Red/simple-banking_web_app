from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, login_manager


app = Flask(__name__)
app.config['SECRET_KEY'] = "hellowoorrlllddd"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SBWA.db'

# db = SQLAlchemy(app)

# from .models import Users


# login_manager = LoginManager()
# login_manager.login_view = 'login'
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(id):
#     return Users.query.get(int(id))

from SBWA import routes