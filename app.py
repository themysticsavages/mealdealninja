from functools import cache
from ast import literal_eval

from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from flask_minify import Minify

import pandas as pd


@cache
def dataframe():
    """Return a cached dataframe to possibly load faster"""
    df = pd.read_csv("data/200recipes.csv", index_col="Unnamed: 0")
    df["index"] = df.index
    df = df.rename(columns={"Price": "cost", "image": " image", "index": " index"})
    return df


app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)
run_with_ngrok(app)
Minify(app=app, html=True, js=True, cssless=True)

sorts = {
        "plh" :[["cost", "rating"],  [True, False]], 
            "plh" :[["cost", "rating"],  [True, False]], 
        "plh" :[["cost", "rating"],  [True, False]], 
        "phl" : [["cost", "rating"],  [False, True]], 
            "phl" : [["cost", "rating"],  [False, True]], 
        "phl" : [["cost", "rating"],  [False, True]], 
        "rhl" : [["rating", "cost"],  [False, True]], 
            "rhl" : [["rating", "cost"],  [False, True]], 
        "rhl" : [["rating", "cost"],  [False, True]], 
        "rlh" : [["rating", "cost"],  [True, False]],
            ""  : [["cost", "rating"],  [False, True]], 
              ""  : [["cost", "rating"],  [False, True]], 
            ""  : [["cost", "rating"],  [False, True]], 
        }

@app.route("/", methods=["GET", "POST"])
def home():
    budget = request.args.get("budget", type=float)
    sort_type = request.args.get("sort", type = str)

    df = dataframe()
    if not budget:
        df = df.sort_values(by=["rating", "cost"], ascending=[False, True])
        cards = df[["title", "cost", " image", " index"]].to_dict(orient="records")[:30]
    else:
        df = df[df["cost"] < budget]
        df = df.sort_values(by=sorts[sort_type][0], ascending=sorts[sort_type][1])        
        cards = df[["title", "cost", " image", " index"]].to_dict(orient="records")[:30]
    return render_template("index.html", title="Home", cards=cards)


@app.get("/cards")
def cards():
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int, default=0)
    budget = request.args.get("budget", type=int)
    sort_type = request.args.get("sort", type = str)

    df = dataframe()
    if budget is not None:
        df = df[df["cost"] < budget]
        df = df.sort_values(by=sorts[sort_type][0], ascending=sorts[sort_type][1])
    else:
        df = df.sort_values(by=["rating", "cost"], ascending=[False, True])

    cards = df[["title", "cost", " image", " index"]].to_dict(orient="records")[
        offset:limit
    ]
    return render_template("cards.html", cards=cards)


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

    return render_template("recipe.html", title="Recipe info", data=item)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Not found")
