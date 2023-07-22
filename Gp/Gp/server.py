from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/detail')
def about():
    return render_template('inner-page.html')

@app.route('/about')
def detail():
    return render_template('portfolio-details.html')

@app.route('/blog/<content>')
def blog(content):
    respond = define_content(int(content))
    return render_template('inner-page-blog.html', content=respond)

def define_content(cont:int):
    request = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    responds = request.json()
    return responds[cont]

if __name__ == '__main__':
    app.run(debug = True)