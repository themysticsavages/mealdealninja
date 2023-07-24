from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html", title="Home")


@app.get("/about")
def about():
    return render_template("about.html", title="About")


@app.get("/stats")
def stats():
    return render_template("stats.html", title="Statistics")


@app.get("/recipeinfo")
def recipeinfo():
    return render_template("recipe_info.html", title="Recipe info")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Not found")
