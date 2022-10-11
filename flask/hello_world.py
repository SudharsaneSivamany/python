from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/career')
def career():
    return "Have a good career"


@app.route('/red')
def red():
    return redirect(url_for("hello_world"))

if __name__ == '__main__':
    app.run()
