<div align="center">
<img src="static/logo.png">
</div>

# MealDealNinja

A solution to food insecurity by providing simple budget-friendly meals

## How to run

Make sure you have a recent version of [Python](https://www.python.org/downloads/).

Also make sure you have the latest version of the main branch! Some things might have changed

```bash
git checkout main
git pull
git checkout <your branch>
git merge main
```

Then do the following:

**Windows Git Bash**:

```bash
python -m venv env
source ./env/scripts/activate
pip install -r requirements.txt
flask run
```

**Mac OS / Linux**:

```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
flask run
```

The app should be running on [local host five thousand](http://localhost:5000)

If you want to edit a page, just edit stuff inside:

```
{% block content %}
here
{% endblock content %}
```
