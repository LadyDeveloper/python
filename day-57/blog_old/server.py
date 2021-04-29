from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)



@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    random_number = random.randint(0, 36)
    return render_template("index.html", random_number=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):

    # Requesting data from API - https://agify.io/
    res_age = requests.get(url=f"https://api.agify.io?name={name}")

    # Requesting data from API - https://genderize.io/
    res_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    
    return render_template('guess.html', name=name, gender=res_gender, age=res_age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_request = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965")
    blog_data = blog_request.json()
    return render_template('blog.html', posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)