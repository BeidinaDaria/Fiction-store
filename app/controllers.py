import uuid
from app import app, db
from .models import Item, User, Comment
from flask import render_template, request, redirect, make_response, Response
from datetime import datetime

#   APP ROUTING

def authToken(request):
    token = request.cookies.get('token')
    if token and (user := db.session.query(User).filter_by(token=token).first()):
        return user
    return False

def favs_basket_len(user, cookies):
    if user:
        return len(user.favourites), len(user.basket)
    return len(cookies.get('favourites') or "")//2, len(cookies.get('basket') or "")//2


@app.route('/', methods=['GET'])
def index():
    items = db.session.query(Item).limit(5).all()
    best_items = db.session.query(Item).order_by(Item.price).limit(5).all()
    favs_len, basket_len = favs_basket_len(authToken(request), request.cookies)
    return render_template('index.html', favs_len=favs_len, basket_len=basket_len,
                           items=items, best_items=best_items)


@app.route('/product', methods=['GET', 'POST'])
def product():
    id = request.args.get('id')
    if not id or not (item := db.session.query(Item).filter(Item.id == id).first()):
        return redirect("404", code=404), {"Refresh": "0; url=/404"}
    average=0
    if item.comments:
        for comment in item.comments:
            average += comment.score
        average /= len(item.comments)
    user = authToken(request)
    if score := request.form.get('score'):
        pros = request.form.get('pros')
        cons = request.form.get('cons')
        text = request.form.get('text')
        item.comments.append(Comment(user_id=user.id, date=datetime.today().strftime('%d-%Y-%m'),
                                    score=int(score), pros=pros, cons=cons, text=text))
        db.session.commit()
    favs_len, basket_len = favs_basket_len(user, request.cookies)
    if user:
        in_fav = user.favourites.count(item) != 0
        in_basket = user.basket.count(item) != 0
    else:
        in_fav = (favourites := request.cookies.get('favourites')) and id+',' in favourites
        in_basket = (basket := request.cookies.get('basket')) and id+',' in basket
    return render_template('product.html', favs_len=favs_len, basket_len=basket_len,
                           item=item, in_fav=in_fav, in_basket=in_basket,
                           average=average, user=user)


@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    # search
    search = request.args.get('search')
    items = db.session.query(Item).filter(Item.title == search[0].upper()+search[1:].lower()).all() \
            if search else db.session.query(Item).all()
    # filter
    if filter_sci := request.args.getlist('sci'):
        items = [item for item in items for sci in filter_sci if sci in item.science]
    if filter_color := request.args.getlist('color'):
        items = [item for item in items for color in filter_color if color in item.colors]
    if (filter_price_from := request.args.get('price_from')):
        items = [item for item in items if item.price >= int(filter_price_from)]
    if (filter_price_to := request.args.get('price_to')):
        items = [item for item in items if item.price <= int(filter_price_to)]
    favs_len, basket_len = favs_basket_len(authToken(request), request.cookies)
    return render_template('catalog.html', favs_len=favs_len,
                           basket_len=basket_len, items=items,search=search)


@app.route('/favourites')
def favourites():
    if user := authToken(request):
        favourites = user.favourites
    elif (ids := request.cookies.get('favourites')):
        favourites = db.session.query(Item).filter(Item.id.in_(ids.split(',')[:-1])).all()
    else:
        favourites = 0
    favs_len, basket_len = favs_basket_len(user, request.cookies)
    return render_template('favourites.html', favs_len=favs_len,
                           basket_len=basket_len, favourites=favourites)


@app.route('/basket')
def basket():
    if user := authToken(request):
        basket = user.basket
    elif (ids := request.cookies.get('basket')):
        basket = db.session.query(Item).filter(Item.id.in_(ids.split(',')[:-1])).all()
    else:
        basket = 0
    favs_len, basket_len = favs_basket_len(user, request.cookies)
    return render_template('basket.html', favs_len=favs_len,
                           basket_len=basket_len, basket=basket)


@app.route('/profile', methods=['GET'])
def profile():
    # check if not login
    if not (user := authToken(request)):
        return redirect('/login')
    favs_len, basket_len = favs_basket_len(user, False)
    return render_template('profile.html', favs_len=favs_len,
                           basket_len=basket_len, user=user)


# Token Authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    # check if already login
    if (user := authToken(request)):
        return redirect('/profile')
    favs_len, basket_len = favs_basket_len(False, request.cookies)
    # get form data
    email = request.form.get('email')
    password = request.form.get('pwd')
    if not email or not password:
        return render_template('login.html', favs_len=favs_len, basket_len=basket_len)
    if not (user := db.session.query(User).filter_by(email=email, password=password).first()):
        return render_template('login.html', favs_len=favs_len, basket_len=basket_len,
                                message="Неправильный логин или пароль")
    # generate unique token, find user in DB & set token in cookie
    response = make_response(redirect('/profile'))
    while True:
        try:
            user.token = uuid.uuid4().hex
            db.session.commit()
        except Exception as e:
            print(e)
        else:
            response.set_cookie('token', user.token)
            return response


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # check if already login
    if authToken(request):
        return redirect('/profile')
    favs_len, basket_len = favs_basket_len(False, request.cookies)
    # get form data
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('pwd')
    if not email or not username or not password:
        return render_template('registration.html',
                               favs_len=favs_len, basket_len=basket_len)
    if password != request.form.get('pwd-repeat'):
        return render_template('registration.html', message="Введённые пароли не совпадают",
                               favs_len=favs_len, basket_len=basket_len)
    if len(password) < 6:
        return render_template('registration.html', message="Пароль должен быть длинней 6 символов",
                               favs_len=favs_len, basket_len=basket_len)
    if db.session.query(User).filter_by(email=email).first():
        return render_template('registration.html', message="Пользователь с такой почтой уже зарегестрирован",
                               favs_len=favs_len, basket_len=basket_len)
    # generate unique token, add user to DB & set token in cookie
    response = make_response(redirect('/'))
    while True:
        try:
            token = uuid.uuid4().hex
            db.session.add(User(
                email=email, name=username,
                token=token, password=password
            ))
            db.session.commit()
        except Exception as e:
            print(e)
        else:
            response.set_cookie('token', token)
            return response


@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('token')
    return response


@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404


#   AJAX METHODS

def basket_favourites(request, attr_name, method_name):
    # check for item id correctness
    if not request.data.isdigit():
        return Response(status=400)
    if not (user := authToken(request)):
        # if not login
        attr_cookie = request.cookies.get(attr_name)
        request_data = str(request.data, 'utf-8')+','
        response = Response(status=200)
        if method_name == "append":
            # if already setted in cookie we don't need to set twice
            if attr_cookie and request_data in attr_cookie:
                return Response(status=412)
            response.set_cookie(attr_name, (attr_cookie or "")+request_data)
        else:
            # if not setted in cookie we can't remove it from there
            if not attr_cookie or not (request_data in attr_cookie):
                return Response(status=412)
            response.set_cookie(attr_name, attr_cookie.replace(request_data, ''))
        return response
    method = getattr(getattr(user, attr_name), method_name)
    try:
        method(db.session.query(Item).filter_by(id=int(request.data)).first())
        db.session.commit()
    except Exception as e:
        print(e)
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
