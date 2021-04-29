from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blogs = Post()

@app.route('/')
def home():
    blog_data = blogs.get_all_blogs()
    return render_template("index.html", blogs=blogs.get_all_blogs())

@app.route('/blog/<id>')
def get_blog(id):
    return render_template("post.html", blog=blogs.get_blog(id))

if __name__ == "__main__":
    app.run(debug=True)
