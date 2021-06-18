from app import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    amount = db.Column(db.Integer, default=10) # how many books are ordered
    order_date = db.Column(db.Datetime(), default=datetime.now)

    @property
    def __serialize__(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "amount": self.amount,
            "order_date": self.order_date
        }