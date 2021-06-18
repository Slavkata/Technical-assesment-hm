from API import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=10) # how many books are available for sale

    @property
    def __serialize__(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "quantity": self.quantity
        }