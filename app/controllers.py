from app import app, db
from .models import Item, User
from flask import render_template, request, redirect, make_response, Response

#   APP ROUTING

def authToken(request):
    token = request.cookies.get('token')
    if not token or not (user := db.session.query(User).filter_by(token=token).first()):
        return False
    else:
        return user

def favs_basket_len(user):
    if user:
        return len(user.favourites), len(user.basket)
    else:
        # TODO: get from cookies
        return 0, 0


@app.route('/', methods=['GET'])
def index():
    items = db.session.query(Item).limit(5).all()
    # TODO: Пока что сортировка по цене, а не рейтингу в комментариях
    best_items = db.session.query(Item).order_by(Item.price).limit(5).all()
    favs_len, basket_len = favs_basket_len(authToken(request))
    return render_template('index.html', favs_len=favs_len,
                           basket_len=basket_len, items=items,
                           best_items=best_items)


@app.route('/product', methods=['GET'])
def product():
    req = request.args.get('id')
    if not req or not (item := db.session.query(Item).filter(Item.id == req).first()):
        return redirect("404", code=404), {"Refresh": "0; url=/404"}
    user = authToken(request)
    if user:
        in_fav = user.favourites.count(item) != 0
        in_basket = user.basket.count(item) != 0
        favs_len, basket_len = favs_basket_len(user)
    else:
        # get from cookies
        in_fav = 0
        in_basket = 0
        favs_len, basket_len = favs_basket_len(False)
    return render_template('product.html', favs_len=favs_len,
                           basket_len=basket_len, item=item,
                           in_fav=in_fav, in_basket=in_basket)


@app.route('/catalog', methods=['GET'])
def catalog():
    req = request.args.get('search')
    items = db.session.query(Item).filter(Item.title == req[0].upper()+req[1:].lower()).all() \
            if req else db.session.query(Item).all()
    favs_len, basket_len = favs_basket_len(authToken(request))
    # TODO: Добавить вёрстку в случае, когда по запросу ничего не найдено
    return render_template('catalog.html', favs_len=favs_len,
                           basket_len=basket_len, items=items)


@app.route('/favourites')
def favourites():
    user = authToken(request)
    favs_len, basket_len = favs_basket_len(user)
    if user:
        favourites=user.favourites
    else:
        # get from cookies
        favourites=None
    return render_template('favourites.html', favs_len=favs_len,
                           basket_len=basket_len, favourites=favourites)


@app.route('/basket')
def basket():
    user = authToken(request)
    favs_len, basket_len = favs_basket_len(user)
    if user:
        basket=user.basket
    else:
        # get from cookies
        basket=None
    return render_template('basket.html', favs_len=favs_len,
                           basket_len=basket_len, basket=basket)


@app.route('/profile', methods=['GET'])
def profile():
    # check if not login
    user = authToken(request)
    if not user:
        return redirect('/login')
    favs_len, basket_len = favs_basket_len(user)
    return render_template('profile.html', favs_len=favs_len,
                           basket_len=basket_len, user=user)


# JWT Token Authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    # check if already login
    user = authToken(request)
    if user:
        return redirect('/profile')
    favs_len, basket_len = favs_basket_len(False)
    # get data from the form
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        return render_template('login.html', favs_len=favs_len,
                               basket_len=basket_len)
    # find user in DB & set token in cookie
    if (user := db.session.query(User).filter_by(email=email, password=password).first()):
        response = make_response(redirect('/profile'))
        response.set_cookie('token', user.token)
        return response
    return render_template('login.html', favs_len=favs_len,
                           basket_len=basket_len,
                           message="Неправильный логин или пароль")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('registration.html')


@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404


#   AJAX METHODS

def basket_favourites(request, attr_name, method_name):
    if not request.data.isdigit():
        return Response(status=400)
    if not (user := authToken(request)):
        # TODO: set in/get from cookie
        return Response(status=200)
    method = getattr(getattr(user, attr_name), method_name)
    try:
        method(db.session.query(Item).filter_by(id=int(request.data)).one())
        db.session.commit()
    except ValueError:
        return Response(status=412)
    return Response(status=200)

@app.route('/favourites/add', methods=['POST'])
def favourites_add():
    return basket_favourites(request, "favourites", "append")

@app.route('/favourites/remove', methods=['POST'])
def favourites_remove():
    return basket_favourites(request, "favourites", "remove")

@app.route('/basket/add', methods=['POST'])
def basket_add():
    return basket_favourites(request, "basket", "append")

@app.route('/basket/remove', methods=['POST'])
def basket_remove():
    return basket_favourites(request, "basket", "remove")
