from export import export_markdown
import os

FOLDER = "./recipes"


def pathify(name, ext):  # example: pathify("Cheese Cake",".md")
    return name.replace(" ", "-").replace(".", "-").replace("/", "-") + ext


if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

recipes = export_markdown()

for recipe in recipes:
    with open(
        os.path.join(FOLDER, pathify(recipe["name"], ".md")),
        "w",
    ) as f:
        f.write(recipe["text"])


text = """<title>Recipes</title>
# Recipes

* * *

"""
for recipe in recipes:
    text += f'* [{recipe["name"]}]({pathify(recipe["name"],".html")})\n'

text += """
* * *

"""

with open(os.path.join(FOLDER, "index.md"), "w") as f:
    f.write(text)
