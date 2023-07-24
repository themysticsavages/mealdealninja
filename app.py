from functools import cache
from ast import literal_eval

from flask import Flask, render_template, send_from_directory
from flask_ngrok import run_with_ngrok

import pandas as pd


@cache
def dataframe():
    """Return a cached dataframe to possibly load faster"""
    df = pd.read_csv("data/200recipes.csv", index_col="Unnamed: 0")
    df["index"] = df.index
    return df


app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)
run_with_ngrok(app)


@app.get("/")
def home():
    df = dataframe()
    df = df.sort_values(by=["rating", "Price"], ascending=[False, True])
    df = df.rename(columns={"Price": "cost", "image": " image", "index": " index"})
    cards = df[["title", "cost", " image", " index"]].to_dict(orient="records")[:30]
    return render_template("index.html", title="Home", cards=cards)


@app.get("/about")
def about():
    return render_template("about.html", title="About")


@app.get("/stats")
def stats():
    return render_template("stats.html", title="Statistics")


@app.get("/recipe/<recipe_id>")
def recipeinfo(recipe_id):
    recipe_id = int(recipe_id)
    df = dataframe()
    item = df.iloc[recipe_id].to_dict()

    for key, value in item.copy().items():
        try:
            item[key] = literal_eval(value)
        except ValueError:
            pass
        except SyntaxError:
            pass
    print(item)

    return render_template("recipe.html", title="Recipe info", data=item)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Not found")
