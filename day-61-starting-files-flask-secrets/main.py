from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import wtforms.validators as validators
import os
SECRET_KEY = os.urandom(32)


class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), validators.Length(min=6, max=120), validators.Email()])
    password = PasswordField('password', validators=[DataRequired()])
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

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
