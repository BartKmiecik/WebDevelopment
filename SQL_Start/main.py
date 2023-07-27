import sqlite3
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,"
#                " author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)



# id: 1
#
# title: "Harry Potter"
#
# author: "J. K. Rowling"
#
# review: 9.3


@app.route("/")
def create():
    print('test')
    book = Book(
        id=1,
        name="Harry Potter",
        author="J. K. Rowling",
        rating=9.
    )
    with app.app_context():
        db.create_all()

        db.session.add(book)
        db.session.commit()
        print(book)
    return book

create()
# if __name__ == '__main__':
#     app.run()