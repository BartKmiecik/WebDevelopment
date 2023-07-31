from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random():
    with app.app_context():
        db.create_all()
        query = db.session.execute(db.select(Cafe).order_by(Cafe.id))
        cafes = query.all()
        rand = random.randint(0, len(cafes)-1)
        cafe = cafes[rand][0]
        cafe_dict = {"id":cafe.id, "name":cafe.name, "map_url":cafe.map_url, "img_url":cafe.img_url,
                       "location":cafe.location,"seats":cafe.seats, "has_toilet":cafe.has_toilet,
                       "has_wifi":cafe.has_wifi, "has_sockets":cafe.has_sockets, "can_take_calls":cafe.can_take_calls,
                       "coffee_price":cafe.coffee_price}
        db.session.commit()
        return jsonify(cafe=cafe_dict)


@app.route("/all")
def get_all():
    with app.app_context():
        db.create_all()
        query = db.session.execute(db.select(Cafe).order_by(Cafe.id))
        cafes = query.all()
        all_cafes = []
        for cafe in cafes:
            cafe = cafe[0]
            cafe_dict = {"id": cafe.id, "name": cafe.name, "map_url": cafe.map_url, "img_url": cafe.img_url,
                         "location": cafe.location, "seats": cafe.seats, "has_toilet": cafe.has_toilet,
                         "has_wifi": cafe.has_wifi, "has_sockets": cafe.has_sockets,
                         "can_take_calls": cafe.can_take_calls,
                         "coffee_price": cafe.coffee_price}
            all_cafes.append(cafe_dict)
        db.session.commit()
        return jsonify(all_cafes=all_cafes)


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
