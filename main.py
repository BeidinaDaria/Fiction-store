
from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DataBase.database_interaction import Items, Base
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable = False)
    price = db.Column(db.Double, nullable=False)
    description = db.Column(db.Text, nullable=True)
    def __repr__(self):
        return self.title


@app.route('/')
def index():
    items=Item.query.order_by(Item.price).all()
    return render_template('index.html')


@app.route('/catalog')
def about():
    return render_template('catalog.html')


@app.route('/favourites')
def favourites():
    return render_template('favourites.html')


@app.route('/basket')
def basket():
    return render_template('basket.html')


@app.route('/product')
def product():
    return render_template('product.html')

    
    
    
    #   entry point
if __name__ == "__main__":
    # database config and session creating
    engine = create_engine("sqlite:///fiction_store.db")
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # run flask application
    app.run(debug=True)
    # items = session.query(Items).all() # for get all rows from items table