from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# INITIALIZING

# init application
app = Flask(__name__)

# load config
app.config.from_pyfile("config.cfg")

# init database
db = SQLAlchemy(app)

# init controllers
from . import controllers