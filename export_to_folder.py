from export import export_markdown
from markdown import markdown
from json import dumps
import os

FOLDER = "./recipes"


def pathify(name, ext):  # example: pathify("Cheese Cake",".md")
    return name.replace(" ", "-").replace(".", "-").replace("/", "-") + ext


if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

recipes = export_markdown()
print(recipes)

for recipe in recipes:
    with open(
        os.path.join(FOLDER, pathify(recipe["name"], ".md")),
        "w",
    ) as f:
        f.write(recipe["text"])


text = """<title>Recipes</title>
# Recipes
<form action="search.html" method="get">
<input type="search" id="search" name="q">
<input type="submit" value="Search">
</form>

* * *

"""
for recipe in recipes:
    text += f'- **[{recipe["name"]}]({pathify(recipe["name"],".html")})**  \n{recipe["desc"]}\n'

text += """
* * *

"""

with open(os.path.join(FOLDER, "index.md"), "w") as f:
    f.write(text)

jsrecipes = []
for recipe in recipes:
    jsrecipes.append(
        [
            pathify(recipe["name"], ".html"),
            markdown(
                f'- **[{recipe["name"]}]({pathify(recipe["name"],".html")})**  \n{recipe["desc"]}\n'
            ),
            recipe["text"],
        ]
    )

print(jsrecipes)
text = (
    f"""<title>Recipes</title>
<script>
function main(){{
const files={jsrecipes};"""
    + """
document.getElementById("search").value=(new URL(window.location.href)).searchParams.get('q')
const search = (new URL(window.location.href)).searchParams.get('q').toLowerCase().split(" ");
let matches = new Set();
for (let recipe of files) {
    //alert(recipe[0]);
    for (let word of search) {
        //alert(word);
        if (recipe[2].toLowerCase().includes(word)) {
            //alert("Found match: "+recipe[0]);
            matches.add(recipe[1]);
        }
    }
}
let matchArr=[...matches];
const recipes=document.getElementById("recipes");
recipes.innerHTML=matchArr.join("\\n");
if (matchArr.length == 0){
	recipes.innerHTML="No Results Found."
}
}
</script>
<body onload="main()">
# Recipe Search Results
<form action="search.html" method="get">
<input type="search" id="search" name="q">
<input type="submit" value="Search">
</form>

* * *
<div id="recipes">
"""
)
for recipe in recipes:
    text += f'\n- **[{recipe["name"]}]({pathify(recipe["name"],".html")})**  \n{recipe["desc"]}'

text += """
</div>
* * *

</body>
"""

with open(os.path.join(FOLDER, "search.md"), "w") as f:
    f.write(text)
