from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import wtforms.validators as validators
import os
from flask_bootstrap import Bootstrap5
SECRET_KEY = os.urandom(32)


class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), validators.Length(min=6, max=120), validators.Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("Login")


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        _email = form.email.data
        _password = form.password.data
        print(f'{_email} and {_password}')
        if _email == 'admin@email.com' and _password == '12345678':
            return redirect('/success')
        else:
            return redirect('denied')
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
