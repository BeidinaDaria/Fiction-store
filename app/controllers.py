from app import app, db
from flask import render_template, request
from .models import Items


#   APP ROUTING

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/catalog', methods=['GET'])
def catalog():
    req = request.args.get('search')
    if req:
        items = db.session.query(Items).filter(Items.title == req).all()
        return str(items)
    else:
        return render_template('catalog.html')

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
