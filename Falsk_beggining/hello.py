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

from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home_index():
    return 'Home page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/username/<user>')
def greet_user(user):
    return f'Hello {user}'

if __name__ == "__main__":
    app.run(debug=True)

