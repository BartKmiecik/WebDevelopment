from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)
ckeditor = CKEditor(app)

# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# with app.app_context():
#     db.create_all()

class BlogPostForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    subtitle = StringField("subtitle", validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    background_url = StringField('background_url')
    body = CKEditorField("body")
    submit = SubmitField()

@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    with app.app_context():
        db.create_all()
        query = db.session.execute(db.select(BlogPost).order_by(BlogPost.id))
        blog_posts = query.all()
        for post in blog_posts:
            posts.append(post[0])
        # db.session.commit()
        print(posts)
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = "Grab the post from your database"
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post

@app.route('/new_post', methods=["GET", "POST"])
def new_post():
    form = BlogPostForm()
    # form.body.data = get_the_article_body_from_somewhere()
    if form.validate():
        query = db.session.execute(db.select(BlogPost).order(BlogPost.id))
        blog_posts = query.all()
        idx = blog_posts[-1].id + 1
        new_post = BlogPost(
            body = form.body.data,
            id = idx,
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = 'July 21 2023',
            author = form.author.data,
            img_url = form.background_url.data
        )
        with app.app_context():
            db.create_all()
            db.session.add(new_post)
            db.session.commit()

    return render_template('make-post.html', form=form)

# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
