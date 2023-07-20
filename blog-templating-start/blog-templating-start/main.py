from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/post/<post>')
def get_post(post):
    request = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    print(request)
    return render_template("post.html", post=request.json()[int(post)])

if __name__ == "__main__":
    request = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    print(request.json())
    app.run(debug=True)
