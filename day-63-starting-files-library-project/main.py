from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
all_books = []
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)

@app.route('/')
def home():
    with app.app_context():
        db.create_all()
        all_books = Book.query.order_by(Book.id).all()
    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    # form = Books()
    # if form.validate():
    #     print('validate')
    #     print(form)
    #    # print(form.title)
    #     all_books.append({'title': form.title, 'author': form.author, 'rating': form.rating})
    #
    # len(all_books)
    # print('test')
    if request.method == 'POST':
        # book = Book(
        #     id=1,
        #     name="Harry Potter",
        #     author="J. K. Rowling",
        #     rating=9.
        # )

        with app.app_context():
            db.create_all()
            last_book = Book.query.order_by(Book.id).all()
            title = request.form['book']
            author = request.form['author']
            rating = request.form['rating']

            book = Book(
                id= last_book[-1].id+1,
                name=title,
                author=author,
                rating=rating
            )
            db.session.add(book)
            db.session.commit()

    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)


# import sqlite3
# from flask import Flask, request


# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,"
#                " author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# create the extension


