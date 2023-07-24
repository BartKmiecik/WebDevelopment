from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
SECRET_KEY = os.urandom(32)


class MyForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField("Login")


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
