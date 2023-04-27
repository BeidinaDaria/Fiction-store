from app import db

#   MODEL OF BASKET AND FAVOURITES TABLES

basket = db.Table("basket",
            db.Column("user_id", db.Integer, db.ForeignKey('user.id')),
            db.Column("item_id", db.Integer, db.ForeignKey('item.id'))
)
favourites = db.Table("favourites",
            db.Column("user_id", db.Integer, db.ForeignKey('user.id')),
            db.Column("item_id", db.Integer, db.ForeignKey('item.id'))
)

#   MODEL OF ITEMS TABLE

class Item(db.Model):
    __tablename__ = "item"
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(100), nullable=False)
    price           = db.Column(db.Float, nullable=False)
    description     = db.Column(db.String(1000), nullable=False)
    images          = db.Column(db.JSON) # [ "str", ... ]
    colors          = db.Column(db.JSON) # [ "str", ... ]
    science         = db.Column(db.String(50))
    comments        = db.relationship("Comment", backref="item")

#   MODEL OF USERS TABLE

class User(db.Model):
    __tablename__ = "user"
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(100), nullable=False, unique=True)
    password    = db.Column(db.String(100), nullable=False)
    token       = db.Column(db.String(100), nullable=False, unique=True)
    name        = db.Column(db.String(50), nullable=False)
    surname     = db.Column(db.String(50))
    comments    = db.relationship("Comment", backref="user")
    basket      = db.relationship("Item", secondary=basket, backref=db.backref('users_have_basket'))
    favourites  = db.relationship("Item", secondary=favourites, backref=db.backref('users_have_fav'))

#   MODEL OF COMMENTS TABLE

class Comment(db.Model):
    __tablename__ = "comment"
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))
    item_id     = db.Column(db.Integer, db.ForeignKey('item.id'))
    date        = db.Column(db.String(10), nullable=False) # "day.month.year"
    score       = db.Column(db.Integer, nullable=False)
    pros        = db.Column(db.String(400))
    cons        = db.Column(db.String(400))
    text        = db.Column(db.String(800))
