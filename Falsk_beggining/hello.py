# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
# if __name__ == "__main__":
#     app.run()

import time

def time_decoratr(fun):
    start = time.time()
    fun()
    end = time.time()
    running_time = end - start
    print(running_time)

@time_decoratr
def do_smt():
    time.sleep(1)

while True:
    pass