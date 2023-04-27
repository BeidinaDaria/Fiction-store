from app import db

#   MODEL OF ITEMS TABLE

class Items(db.Model):
    __tablename__ = "items"
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(100), nullable=False)
    price       = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    images      = db.Column(db.JSON) # [ "str", ... ]
    colors      = db.Column(db.JSON) # [ "str", ... ]
    science     = db.Column(db.String(50))
    comments    = db.relationship("Comments", backref="item")

#   MODEL OF USERS TABLE

class Users(db.Model):
    __tablename__ = "users"
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(100), nullable=False, unique=True)
    password    = db.Column(db.String(100), nullable=False)
    token       = db.Column(db.String(100))
    name        = db.Column(db.String(50), nullable=False)
    surname     = db.Column(db.String(50))
    comments    = db.relationship("Comments", backref="user")

#   MODEL OF COMMENTS TABLE

class Comments(db.Model):
    __tablename__ = "comments"
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id     = db.Column(db.Integer, db.ForeignKey('items.id'))
    date        = db.Column(db.String(10), nullable=False) # "day.month.year"
    score       = db.Column(db.Integer, nullable=False)
    pros        = db.Column(db.String(400))
    cons        = db.Column(db.String(400))
    text        = db.Column(db.String(800))
