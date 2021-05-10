from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "anadevmavnuel@gmail.com"
PASSWORD = "cCuiKjXuwg82Whm"


app = Flask(__name__)

data_json = requests.get(url='https://api.npoint.io/0067e63917ca7a5034d9')
data = data_json.json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET","POST"])
def contatc():
    if request.method == 'POST':
        message = "Succesfully sent your message."
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:BLOG MSG\n\n{request.form['fname']}\n{request.form['email']}\n{request.form['phone']}\n{request.form['message']}")
        return render_template('contact.html', msg=message)
    else:
        return render_template('contact.html')

@app.route('/post/<index>')
def get_post(index):
    for post in data:
        if post['id'] == int(index):
            image_jpg = f"img/{post['id']}.jpg"
            return render_template('post.html', post=post, img=image_jpg)


if __name__ == "__main__":
    app.run(debug=True)