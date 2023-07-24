from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import os
SECRET_KEY = os.urandom(32)


class MyForm(FlaskForm):
    name = StringField('name')


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = MyForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
