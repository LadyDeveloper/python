from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, url
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), url()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', validators=[DataRequired()], choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕','☕☕☕☕☕'])
    wifi = SelectField('Wifi Strength Rating', validators=[DataRequired()], choices=['✘', '💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'])
    power = SelectField('Power Socket Availiability',validators=[DataRequired()], choices=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='',  encoding="utf8") as file_CSV:
            data_form = [form.cafe.data, form.location.data, form.open_time.data, form.close_time.data, form.rating.data, form.wifi.data, form.power.data, form.submit.data]
            writer = csv.writer(file_CSV)
            writer.writerow(data_form)
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='',  encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        print(csv_data)
        for row in csv_data:
            print(row)
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
