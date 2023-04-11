import json
from app import app, db
from flask import render_template, request
from .models import Items


#   APP ROUTING

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def product():
    req = request.args.get('id')
    item = db.session.query(Items).filter(Items.id == req).first()
    return render_template('product.html', item=item)

@app.route('/catalog', methods=['GET'])
def catalog():
    req = request.args.get('search')
    items = db.session.query(Items).filter(Items.title == req).all() \
            if req else db.session.query(Items).all()
    # TODO: Добавить вёрстку в случае, когда по запросу ничего не найдено
    return render_template('catalog.html', items=items)

@app.route('/favourites')
def favourites():
    return render_template('favourites.html')

@app.route('/basket')
def basket():
    return render_template('basket.html')

@app.route('/entrance')
def entrance():
    return render_template('entrance.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
