from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from movieSearch import Search_movie
import os

SECRET_KEY = os.urandom(32)
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///best_movies.db"
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)
Bootstrap5(app)
searcher = Search_movie()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String, unique=True, nullable=False)
    img_url = db.Column(db.String, unique=True, nullable=False)

class SearchTitle(FlaskForm):
    title = StringField(validators=[DataRequired()])
    submit = SubmitField()


class MovieUpdate(FlaskForm):
    rating = FloatField(validators=[DataRequired()])
    description = StringField(validators=[DataRequired()])
    submit = SubmitField()

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)


@app.route("/")
def home():
    with app.app_context():
        db.create_all()
        query = db.session.execute(db.select(Movie).order_by(Movie.ranking))
        movies = query
        db.session.commit()
        return render_template("index.html", movies=movies)


@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = SearchTitle()
    if form.validate_on_submit():
        title = form.title.data
        data = searcher.search_movie(title)['results']
        return render_template('select.html', movies=data)
        # title = form.title.data
        # data = searcher.search_movie(title)['results']
        # year = data['release_date'],
        # description = data['overview']
        # rating = data['vote_average']
        # ranking = 9,
        # review = "I liked the water.",
        # img_url = f"https://image.tmdb.org/t/p/w500/{data['backdrop_path']}"
        # with app.app_context():
        #     db.create_all()
        #     query = db.session.execute(db.select(Movie).order_by(Movie.ranking))
        #     movies = query
        #     db.session.commit()

    return render_template("add.html", form=form)

@app.route("/select/<data>" )
def select(data):
    return render_template("select.html", movies=data)

@app.route("/delete/<movie>")
def delete(movie):
    with app.app_context():
        db.create_all()
        db.session.execute(db.delete(Movie).where(Movie.title == movie))
        db.session.commit()
        return home()

@app.route("/edit/<movie>", methods=['POST', 'GET'])
def edit_movie(movie):
    form = MovieUpdate()
    if form.validate_on_submit():
        new_rating = form.rating
        new_description = form.description
        with app.app_context():
            db.create_all()
            query = db.session.execute(db.select(Movie).where(Movie.title == movie))
            _movie = query.first()[0]
            _movie.description = new_description.data
            _movie.rating = new_rating.data
            db.session.commit()
            return home()

    return render_template("edit.html", movie=movie, form=form)


if __name__ == '__main__':
    app.run(debug=True)
