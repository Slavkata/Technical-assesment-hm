from flask_restplus import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

db = SQLAlchemy(app)

from .books.views import books
# from orders.views import orders

app.register_blueprint(books, url_prefix='/books')
# app.register_blueprint(orders, url_prefix='/orders')