from app import db


#   MODEL OF ITEMS TABLE


class Items(db.Model):
    __tablename__ = "items"
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(100), nullable=False)
    price       = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    images      = db.Column(db.JSON)
    colors      = db.Column(db.JSON)
    science     = db.Column(db.String(50))
    comments    = db.Column(db.JSON)