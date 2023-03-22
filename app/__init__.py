from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# init application
app = Flask(__name__)

# load config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app/database/fiction_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init database
db = SQLAlchemy(app)

from . import controllers