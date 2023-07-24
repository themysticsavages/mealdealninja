from functools import cache

from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

import pandas as pd


@cache
def dataframe():
    return pd.read_csv("data/200recipes.csv", index_col="Unnamed: 0")


app = Flask(__name__)
run_with_ngrok(app)


@app.get("/")
def home():
    df = dataframe().sort_values(by=["rating", "Price"], ascending=[False, True])
    df.rename(columns={"Price": "cost"}, inplace=True)
    cards = df[["title", "cost"]].to_dict(orient="records")[:10]
    return render_template("index.html", title="Home", cards=cards)


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
