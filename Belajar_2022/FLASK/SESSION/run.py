from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.permanent_session_lifetime = timedelta(seconds=5)
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if "username" in session:
        return redirect(url_for('user', username=session['username']))
    return render_template("index.html")

@app.route("/<username>")
def user(username):
    if "username" in Session:
        return render_template("user.html", username=session['username'])
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "123456":
            session["username"] = username
            return redirect(url_for("user", username=session["username"]))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)