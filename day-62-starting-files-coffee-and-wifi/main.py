from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    location = StringField('Location', validators=[DataRequired(),URL])
    open_time = StringField('Open', validators=[DataRequired()])
    close_time = StringField('Close', validators=[DataRequired()])
    coffee_rating = SelectField('Coffe_Rating', choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'),
                                                      ('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                                                      ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi_Rating', choices=[('💪', '💪'), ('💪💪', '💪💪'),
                                                       ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'),
                                                       ('💪💪💪💪💪', '💪💪💪💪💪')], validators=[DataRequired()])

    power_rating = SelectField('Power_Rating', choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'),
                                                      ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                                      ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')], validators=[DataRequired()])

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


class Message:
    def __init__(self, data):
        self.cafe_name = data[0]
        self.location = data[1]
        self.open = data[2]
        self.close = data[3]
        self.coffee = data[4]
        self.wifi = data[5]
        self.power = data[6]



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    msg = []
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for row in csv_data:
            temp_msg = Message(row)
            msg.append(temp_msg)
    data = []
    for m in msg:
        if m != msg[0]:
            data.append({'Cafe Name': m.cafe_name, 'Location': m.location, 'Open': m.open,
                     'Close': m.close, 'Coffe': m.coffee, 'Wifi': m.wifi, 'Power': m.power})
    titles = [('Cafe Name', 'Cafe Name'), ('Location', 'Location'), ('Open', 'Open'), ('Close', 'Close'),
              ('Coffe', 'Coffe'), ('Wifi', 'Wifi'), ('Power', 'Power')]

    return render_template('cafes.html', cafes=data, titles=titles)


if __name__ == '__main__':
    app.run(debug=True)
