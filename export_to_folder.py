from export import export_markdown
import os

FOLDER = "./recipes"

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

recipes = export_markdown()

for name, text in recipes.items():
    with open(
        os.path.join(
            FOLDER, name.replace(" ", "-").replace(".", "-").replace("/", "-") + ".md"
        ),
        "w",
    ) as f:
        f.write(text)

text = """<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Recipes</title>
</head>
<body>
<h1>Recipes</h1>
<hr>
<ul>
"""
for name in recipes:
    text += f'<li><a href="{name.replace(" ", "-").replace(".", "-").replace("/", "-") + ".html"}">{name}</a></li>'
text += """</ul>
<hr>
</body>
</html>
"""

text="""# Recipes

* * *

"""
for name in recipes:
    text += f'* [{name}]({name.replace(" ", "-").replace(".", "-").replace("/", "-") + ".html"})\n'

text+="""
* * *

"""

with open(os.path.join(FOLDER, "index.md"), "w") as f:
    f.write(text)
