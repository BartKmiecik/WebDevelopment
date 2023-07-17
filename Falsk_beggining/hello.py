# import time
#
# def time_decoratr(fun):
#     start = time.time()
#     fun()
#     end = time.time()
#     running_time = end - start
#     print(running_time)
#
# @time_decoratr
# def do_smt():
#     time.sleep(1)
#
# while True:
#     pass


from functools import wraps
def make_bold(fun):
    @wraps(fun)
    def decorated_function(*args, **kwargs):
        smt = fun(*args, **kwargs)
        return f'<b>{smt}</b>'
    return decorated_function
def make_en(fun):
    @wraps(fun)
    def decorated_function(*args, **kwargs):
        smt = fun(*args, **kwargs)
        return f'<en>{smt}</en>'
    return decorated_function

def make_u(fun):
    @wraps(fun)
    def decorate_function(*args, **kwargs):
        additional_text = f"{args}" + 'bd'
        return fun(additional_text)
    return decorate_function

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home_index():
    return 'Home page'

@app.route('/hello/')
@make_bold
@make_en
def hello_world():
    return 'Hello, World!'

@app.route('/username/<user>')
@make_u
def greet_user(user):
    return f'Hello {user}'

if __name__ == "__main__":
    app.run(debug=True)

