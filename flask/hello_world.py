from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


# Home page of your website
@app.route('/')
def hello_world():
    return "Hello World"

# Web page for the path /career
@app.route('/career')
def career():
    return "Have a good career"

# Html page for the path /india
# Note the .html file should be placed inside the templates folder. templates folder should exists in the path where the python script exists
@app.route('/india')
def india():
    return render_template("index.html")

# redirects to home page when we hit the path /red
@app.route('/red')
def red():
    return redirect(url_for("hello_world"))

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        return redirect(url_for("user_info", user=username))
    else:
        return render_template("login.html")

@app.route('/<user>')
def user_info(user):
    return f"<h1>Hi {user} !!!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
