from flask import render_template, json, request, jsonify
from app import app
from . import models


#   APP ROUTING
@app.route('/')
def index():
    return render_template('index')

@app.route('/product', methods=['GET', 'POST'])
def search():
    search = request.args.get('search')
    if search:
        items = models.Items.query.all()
        return str(items[0].title)

@app.route('/catalog')
def about():
    return render_template('catalog')


@app.route('/favourites')
def favourites():
    return render_template('favourites')


@app.route('/basket')
def basket():
    return render_template('basket')


# @app.route('/product')
# def product():
#     return render_template('product')
