from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


app = Flask(__name__, template_folder='views/templates')
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)

from app.controllers.email_controller import email_bp
app.register_blueprint(email_bp)