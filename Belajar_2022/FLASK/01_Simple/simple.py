import re

from symbol import return_stmt


@app.routed("/")
def index():
    return "Hello, World!"

@app.route("/anas")
def anas():
    return "Anas!"

@app.route("html")
def more_html():
    return "BRUHHHHHHHHH"