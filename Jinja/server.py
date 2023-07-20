from flask import Flask, render_template
import random
import datetime as dt

app = Flask(__name__)


@app.route('/')
def hello_world():
    rand = random.randint(0,10)
    year = dt.datetime.now()
    return render_template('index.html', rand=rand, year=(year.strftime('%Y')))

@app.route('/guess/{username}')
def hello_world():
    return render_template('index.html', rand=rand, year=(year.strftime('%Y')))


if __name__ == '__main__':
    app.run(debug=True)

