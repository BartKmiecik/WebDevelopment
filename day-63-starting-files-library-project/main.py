from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from wtforms import Form, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

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

all_books = []


# def is_range(field):
#     if field.data >= 10 or field.data < 0:
#         raise ValidationError('Incorrect integer. Pass number from 0 - 10')


class Books(Form):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    rating = IntegerField('rating', validators=[DataRequired()])
    submit = SubmitField()

@app.route('/')
def home():
    # all_books.append({'title': 'HarryPotter', 'author': 'J.K.Rowling', 'rating': 9})
    # all_books.append({'title': 'HarryPotter', 'author': 'J.K.Rowling', 'rating': 7})
    # all_books.append({'title': 'HarryPotter', 'author': 'J.K.Rowling', 'rating': 3})
    print(all_books)
    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = Books()
    if form.validate():
        all_books.append({'title': form.title, 'author': form.author, 'rating': form.rating})

    len(all_books)
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)

