from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()

    christmas = now.month == 12 and now.day == 25 # True / False
    return render_template("index.html", christmas=christmas)

app.run(debug=True)