from app import app, db
from .models import Items, Users
from sqlalchemy import func
from flask import render_template, request, redirect, make_response

#   APP ROUTING

@app.route('/', methods=['GET'])
def index():
    items = db.session.query(Items).limit(5).all()
    # TODO: Пока что сортировка по цене, а не рейтингу в комментариях
    best_items = db.session.query(Items).order_by(Items.price).limit(5).all()
    return render_template('index.html', items=items, best_items=best_items)


@app.route('/product', methods=['GET'])
def product():
    req = request.args.get('id')
    item = db.session.query(Items).filter(Items.id == req).first()
    return render_template('product.html', item=item)


@app.route('/catalog', methods=['GET'])
def catalog():
    req = request.args.get('search')
    items = db.session.query(Items).filter(Items.title == req[0].upper()+req[1:].lower()).all() \
            if req else db.session.query(Items).all()
    # TODO: Добавить вёрстку в случае, когда по запросу ничего не найдено
    return render_template('catalog.html', items=items)


@app.route('/favourites')
def favourites():
    return render_template('favourites.html')


@app.route('/basket')
def basket():
    return render_template('basket.html')


@app.route('/profile', methods=['GET'])
def profile():
    # check if not login
    token = request.cookies.get('token')
    if not token:
        return redirect('/login')
    
    user = db.session.query(Users).filter_by(token=token).first()
    if not user:
        return redirect('/login')
    return render_template('profile.html', user=user)


# JWT Token Authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    # check if already login
    token = request.cookies.get('token')
    if token and db.session.query(Users).filter_by(token=token).first():
        return redirect('/profile')
    # get data from the form
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        return render_template('login.html')
    # search in DB
    user = db.session.query(Users).filter_by(email=email, password=password).first()
    # set token in cookie
    if user:
        response = make_response(redirect('/profile'))
        response.set_cookie('token', user.token)
        return response
    return render_template('login.html', message="Неправильный логин или пароль")
