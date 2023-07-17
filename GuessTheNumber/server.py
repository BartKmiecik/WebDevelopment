from flask import Flask
import random
app = Flask(__name__)

rand_nr = random.randint(1, 10)
@app.route('/')
def hello_world():
    return f"<h1>Guess a number between 0 and 9         {rand_nr}</h1>" \
           "<img src = https://media.giphy.com/media/xoHntNXFYkfzGAftEv/giphy.gif>"

def to_hight():
    return f'<h1>Too high</h1>' \
           f'<img src = https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>'
def correct():
    return f'<h1>Correct</h1>' \
           f'<img src = https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>'

def too_low():
    return f'<h1>To low</h1>' \
           f'<img src = https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gifhttps://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>'

@app.route('/<int:g_number>')
def guess(g_number):
    if g_number > rand_nr:
        return to_hight()
    if g_number < rand_nr:
        return too_low()
    return correct()


if __name__ == '__main__':
    app.run(debug=True)