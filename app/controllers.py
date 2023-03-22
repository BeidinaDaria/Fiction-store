from flask import render_template
from app import app


#   APP ROUTING
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