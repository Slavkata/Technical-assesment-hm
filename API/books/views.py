from flask import Blueprint
from flask_restplus import reqparse
from datetime import datetime
from flask import jsonify

# Specific imports
from .models import Book
from API import api, db

books = Blueprint("books", __name__)

@books.route('/', methods=['GET'])
@api.expect()
def get_books():
    books = [b.__serialize__ for b in db.session.query(Book).all()]
    return jsonify(books)