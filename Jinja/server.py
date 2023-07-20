from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

def get_age(name:str):
    request = requests.get(f'https://api.agify.io?name={name}')
    return request.text.split(',')[2][6:-1]


def get_sex(name:str):
    request = requests.get(f'https://api.genderize.io?name={name}')
    return request.text.split(',')[2][10:-1]

@app.route('/')
def hello_world():
    rand = random.randint(0,10)
    year = dt.datetime.now()
    return render_template('index.html', rand=rand, year=(year.strftime('%Y')))


@app.route('/guess/<username>')
def guess_human(username):
    name = username
    old = get_age(username)
    sex = get_sex(username)
    return render_template('guess.html', name=name, sex=sex, old=old)

@app.route('/blog')
def blog():
    url = 'https://api.npoint.io/c790b4d5cab58020d391'
    request = requests.get(url)

    return render_template('blog.html', blog=request.json())



if __name__ == '__main__':
    app.run(debug=True)

