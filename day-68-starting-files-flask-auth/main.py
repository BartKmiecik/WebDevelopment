import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = 'static/files'
# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
# with app.app_context():
#     db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        with app.app_context():
            db.create_all()
            try:
                query = db.session.execute(db.select(User).order_by(User.id))
                user = query.all()
                idx = user[-1][0].id + 1
            except:
                print('No users in database, assignee id = 1')
                idx = 1

            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password', 'pbkdf2')
            new_user = User(
                id=idx,
                name=name,
                email=email,
                password=werkzeug.security.generate_password_hash(password)
            )
            db.session.add(new_user)
            db.session.commit()
            return render_template("secrets.html", name=new_user.name)

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == "POST":
        # Login and validate the user.
        # user should be an instance of your `User` class
        password = request.form.get('password')
        email = request.form.get('email')
        print(email, password)

        with app.app_context():
            db.create_all()
            user = db.first_or_404(db.select(User).where(User.email == email), description='User not om db')
            print(user)
            print(user.id)
            print(user.email)
            password_correct = werkzeug.security.check_password_hash(user.password, password)
            print(password_correct)
            db.session.commit()
            if password_correct:
                login_user(user)
                return redirect('/secrets')

        # flask.flash('Logged in successfully.')
        #
        # next = flask.request.args.get('next')
        # # url_has_allowed_host_and_scheme should check if the url is safe
        # # for redirects, meaning it matches the request host.
        # # See Django's url_has_allowed_host_and_scheme for an example.
        # if not url_has_allowed_host_and_scheme(next, request.host):
        #     return flask.abort(400)
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/download', methods=['GET'])
@login_required
def download():
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf'
    )


if __name__ == "__main__":
    app.run(debug=True)
