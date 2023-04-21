from app import db


#   MODEL OF Users TABLE


class User(db.Model):
    __tablename__ = "users"
    id          = db.Column(db.Integer, primary_key=True)
    login       = db.Column(db.String(100), nullable=False)
    password    = db.Column(db.String(100), nullable=False)
    name        = db.Column(db.String(100), nullable=False)
    surname     = db.Column(db.String(100), nullable=False)
    comments    = db.Column(db.JSON)