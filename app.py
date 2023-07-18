from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/stats")
def stats():
    return render_template("stats.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")
