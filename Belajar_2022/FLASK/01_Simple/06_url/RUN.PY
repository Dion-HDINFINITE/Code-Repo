from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("index.html", names=names)

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/<string:file>")
def html_file(file):
    return render_template(f"htmls/{file}")

if __name__ == '__main__':
    app.run(debug=True)