# MealDealNinja

The app of all time in the time of all the times in time

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

**Windows Powershell**:

```bash
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
flask run
```

**Mac OS / Linux**:

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
flask run
```

The app should be running on [http://localhost:5000](http://localhost:5000)
