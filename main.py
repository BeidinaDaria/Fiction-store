from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DataBase.database_interaction import Items, Base


app = Flask(__name__)

@app.route('/')
def index():
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
