import requests
from bs4 import BeautifulSoup

widget = requests.post(
    "https://api.spoonacular.com/recipes/visualizePriceEstimator",
    data={
        "apiKey": "17a880d8a40f4451bccdc80f4d3aa38e",
        "ingredientList": "1 apple\n2 cups of coffee\n1.4 liters almond milk\n2 1/2 salmon fillets",
        "servings": "1",
        "defaultCss": "false",
    },
)
soup = BeautifulSoup(widget.text, "html.parser")
things = soup.select_one("#spoonacularPriceBreakdownTable").find_all("div")

items = repr(things[2]).split("<br/>")[1:-1]
prices = repr(things[3]).split("<br/>")[1:-1]

ingredients = dict(zip(items, prices))
print(ingredients)
