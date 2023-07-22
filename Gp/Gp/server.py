from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug = True)