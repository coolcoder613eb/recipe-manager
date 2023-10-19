from recipes import load_recipes as load, save_recipes as save


def export_markdown():
    recipes_json = load()
    recipes_md = {}
    for recipe in recipes_json["recipes"]:
        md_text= "# " + recipe["name"] + "\n"
        md_text+= recipe["desc"] + "  \n"
        if 'recipes' in recipe:
            for subrecipe in recipe['recipes']:
                md_text+=do_recipe(subrecipe)
        md_text+=do_recipe(recipe,'')
        recipes_md[recipe["name"]] = md_text
    return recipes_md


def do_recipe(recipe, extra="#"):
    md_text=''
    if extra:
        md_text += f"{extra}# " + recipe["name"] + "\n"
    if "ingredients" in recipe:
        md_text += f"{extra}## Ingredients\n"
        for ingredient in recipe["ingredients"]:
            md_text += "- " + ingredient + "  \n"
    if "instructions" in recipe:
        md_text += f"{extra}## Instructions\n"
        md_text += recipe['instructions'].replace('\n',"  \n") + "  \n"
    return md_text
