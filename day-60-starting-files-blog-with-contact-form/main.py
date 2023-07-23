from flask import Flask, render_template, request
import requests
from smtplib import SMTP

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)
email = 'mlodybartus@gmail.com'
password = 'tkelpunbstudhbgo'

def send_email(subj, msg, to_email):
    with SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(email, password=password)
        smtp.sendmail(msg=f'{subj}\n\n {msg}', from_addr=email, to_addrs=to_email)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        to_email = request.form['email']
        phone = request.form['phone']
        entry = request.form['message']
        # print(f'{name} {email} {phone} {entry}')
        subject = f'Subject:Hi {name}'
        msg = f'You sent me msg, Your phone is {phone}\n Message: {entry}'
        print(msg)
        send_email(subject,msg, to_email)
        return render_template("contact.html", contact='Successfully sent message!')

    return render_template("contact.html", contact='Contact Me')

# @app.route('/form_entry', methods=['POST'])
# def form_entry():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     entry = request.form['message']
#     print(f'{name} {email} {phone} {entry}')
#     return f'<h1>{entry}</h1>'


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
