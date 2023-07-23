from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login/<user>')
def login_page(user):
    return render_template('login_page.html', user=user)


if __name__ == '__main__':
    app.run()