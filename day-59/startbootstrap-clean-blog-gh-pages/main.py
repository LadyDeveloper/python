from flask import Flask, render_template
import requests

app = Flask(__name__)

data_json = requests.get(url='https://api.npoint.io/0067e63917ca7a5034d9')
data = data_json.json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contatc():
    return render_template('contact.html')

@app.route('/post/<index>')
def get_post(index):
    for post in data:
        print(post['id'], index)
        print(type(post['id']), type(index))
        if post['id'] == int(index):
            image_jpg = f"img/{post['id']}.jpg"
            return render_template('post.html', post=post, img=image_jpg)


if __name__ == "__main__":
    app.run(debug=True)