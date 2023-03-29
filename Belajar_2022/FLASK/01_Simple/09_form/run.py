from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    name = request.args.get("name")
    return render_template("hello.html", name=name)

@app.route("/search")
def search():

    query = request.args.get("query")

    if query:
        return redirect("https://www.google.com/search?q"+query)

    return render_template("search.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "123456":
            return render_template("success.html")
        return render_template("failed.html")

    return render_template("login.html")

@app.route("/authn", methods=["GET", "POST"])
def auth():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "123456":
            return render_template("success.html")
        return render_template("failed.html")

    return render_template("login.html")

