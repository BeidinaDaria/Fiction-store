from app import app, db
from .models import Item, User
from flask import render_template, request, redirect, make_response

#   APP ROUTING

@app.route('/', methods=['GET'])
def index():
    items = db.session.query(Item).limit(5).all()
    # TODO: Пока что сортировка по цене, а не рейтингу в комментариях
    best_items = db.session.query(Item).order_by(Item.price).limit(5).all()

    return render_template('index.html', favs_len=10, basket_len=10, items=items, best_items=best_items)


@app.route('/product', methods=['GET'])
def product():
    req = request.args.get('id')
    if req:
        item = db.session.query(Item).filter(Item.id == req).first()
        if item:
            return render_template('product.html', favs_len=10, basket_len=10, item=item)
    return "Page not found", 404


@app.route('/catalog', methods=['GET'])
def catalog():
    req = request.args.get('search')
    items = db.session.query(Item).filter(Item.title == req[0].upper()+req[1:].lower()).all() if req \
        else db.session.query(Item).all()
    # TODO: Добавить вёрстку в случае, когда по запросу ничего не найдено
    return render_template('catalog.html', favs_len=10, basket_len=10, items=items)


@app.route('/favourites')
def favourites():
    # check if not login
    token = request.cookies.get('token')
    if not token:
        return render_template('favourites.html', favs_len=10, basket_len=10)
    # find user in DB
    favourites = db.session.query(User).filter_by(token=token).first().favourites
    return render_template('favourites.html', favs_len=10, basket_len=10, favourites=favourites)


@app.route('/basket')
def basket():
    # check if not login
    token = request.cookies.get('token')
    if not token:
        return render_template('basket.html', favs_len=10, basket_len=10)
    # find user in DB
    basket = db.session.query(User).filter_by(token=token).first().basket
    return render_template('basket.html', favs_len=10, basket_len=10, basket=basket)


@app.route('/profile', methods=['GET'])
def profile():
    # check if not login
    token = request.cookies.get('token')
    if not token:
        return redirect('/login')
    # find user in DB
    user = db.session.query(User).filter_by(token=token).first()
    if not user:
        return redirect('/login')
    return render_template('profile.html', favs_len=10, basket_len=10, user=user)


# JWT Token Authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    # check if already login
    token = request.cookies.get('token')
    if token and db.session.query(User).filter_by(token=token).first():
        return redirect('/profile')
    # get data from the form
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        return render_template('login.html', favs_len=10, basket_len=10)
    # find user in DB
    user = db.session.query(User).filter_by(email=email, password=password).first()
    # set token in cookie
    if user:
        response = make_response(redirect('/profile'))
        response.set_cookie('token', user.token)
        return response
    return render_template('login.html', favs_len=10, basket_len=10, message="Неправильный логин или пароль")
