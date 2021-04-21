from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_by():
    return 'Bye!'

@app.route('/<names>')
def greet(name):
    return f"Hello {name}\nHow are you doing today?"

if __name__ == '__main__':
    app.run(debug=True)