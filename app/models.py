from sqlalchemy import Column, Integer, String, Float, JSON
from app import db


#   MODEL OF ITEMS TABLE
class Items(db.Model):
    __tablename__ = "items"
    id          = Column(Integer, primary_key=True)
    title       = Column(String(100), nullable=False)
    price       = Column(Float, nullable=False)
    description = Column(String(1000), nullable=False)
    images      = Column(JSON)
    color       = Column(JSON)
    science     = Column(String(50))
    comments    = Column(JSON)