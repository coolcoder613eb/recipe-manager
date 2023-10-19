import json

DEFAULT_RECIPE = "recipes.json"
file = DEFAULT_RECIPE


def load_recipes():
    with open(file, "r", encoding="utf8") as f:
        return json.loads(f.read())


def save_recipes(recipes):
    with open(file, "w", encoding="utf8") as f:
        f.write(json.dumps(recipes))
