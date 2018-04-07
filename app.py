#importing all of the necessary equipment
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def root():
    return render_template("root.html")

@app.route("/basics", methods = ["GET", "POST"])
def basics():
    return render_template("basics.html")

@app.route("/neo", methods = ["GET", "POST"])
def neo():
    return render_template("neo.html")

@app.route("/cyph", methods = ["GET", "POST"])
def cyph():
    return render_template("cyph.html")

@app.route("/other", methods = ["GET", "POST"])
def other():
    return render_template("other.html")

@app.route("/sources", methods = ["GET", "POST"])
def sources():
    return render_template("sources.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
