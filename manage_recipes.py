import json
import sys
import subprocess

FILE_PATH = "recipes.json"

def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {"recipes": []}

def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def edit_text(name):
    while True:
        if sys.platform == "nt":
            subprocess.call([os.path.join(FOLDER, "hecto.exe"), name])
        else:
            subprocess.call(["nano", "-R", "-m", "-n", name])
        try:
            with open(name, "r") as f:
                text = f.read()
                assert text
                break
        except Exception as e:
            continue
    return text

def list_recipes(data, parent_name=None):
    for i, recipe in enumerate(data["recipes"], start=1):
        if parent_name is None:
            print(f"{i}. {recipe['name']} - {recipe['desc']}")
        else:
            print(f"{parent_name} -> {i}. {recipe['name']} - {recipe['desc']}")

def create_recipe(data):
    name = input("Enter the name of the recipe: ")
    desc = input("Enter the description: ")
    is_subrecipe = False #input("Is it a sub-recipe? (yes/no): ").lower() == "yes"

    if is_subrecipe:
        parent_index = int(input("Enter the index of the parent recipe: ")) - 1
        parent_recipe = data["recipes"][parent_index]
        parent_recipe.setdefault("subrecipes", []).append({"name": name, "desc": desc})
        save_data(data)
        print("Sub-recipe added successfully.")
    else:
        
        print("Enter the ingredients, one per line, then save and exit.")
        input("Press Enter to start.")
        text=edit_text('name')
        ingredients=text.splitlines()
        
        print("Enter the instructions, then save and exit.")
        input("Press Enter to start.")
        instructions=edit_text('name')

        recipe = {
            "name": name,
            "desc": desc,
            "ingredients": [ing.strip() for ing in ingredients],
            "instructions": instructions
        }

        data["recipes"].append(recipe)
        save_data(data)
        print("Recipe added successfully.")

def read_recipe(data, index):
    try:
        recipe = data["recipes"][index]
        print(f"Name: {recipe['name']}")
        print(f"Description: {recipe['desc']}")
        print("Ingredients:")
        for ingredient in recipe.get("ingredients", []):
            print(f"- {ingredient}")
        print(f"Instructions: {recipe['instructions']}")

        if "subrecipes" in recipe:
            print("Sub-recipes:")
            list_recipes({"recipes": recipe["subrecipes"]}, parent_name=recipe["name"])
    except IndexError:
        print("Recipe not found.")

def update_recipe(data, index):
    try:
        recipe = data["recipes"][index]
        print(f"Editing {recipe['name']}:")
        name = input("Enter the name of the recipe: ")
        recipe["name"] = name if name else recipe["name"]
        desc = input(f"Enter the description (Current: {recipe['desc']}): ")
        recipe["desc"] = desc if desc else recipe["desc"]
        if "ingredients" in recipe:
            print("Enter the ingredients, one per line, then save and exit.")
            input("Press Enter to start.")
            text=edit_text('name')
            recipe["ingredients"]=text.splitlines()
        if "instructions" in recipe:
            print("Enter the instructions, then save and exit.")
            input("Press Enter to start.")
            recipe["instructions"]=edit_text('name')
        save_data(data)
        print("Recipe updated successfully.")
    except IndexError:
        print("Recipe not found.")

def delete_recipe(data, index):
    try:
        recipe = data["recipes"][index]
        confirmation = input(f"Are you sure you want to delete {recipe['name']}? (yes/no): ")
        if confirmation.lower() == "yes":
            del data["recipes"][index]
            save_data(data)
            print("Recipe deleted successfully.")
        else:
            print("Deletion canceled.")
    except IndexError:
        print("Recipe not found.")

if __name__ == "__main__":
    data = load_data()

    while True:
        print("\nRecipe Manager\n")
        print("1. List recipes")
        print("2. Create a recipe")
        print("3. Read a recipe")
        print("4. Update a recipe")
        print("5. Delete a recipe")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            list_recipes(data)
        elif choice == "2":
            create_recipe(data)
        elif choice == "3":
            index = int(input("Enter the index of the recipe: ")) - 1
            read_recipe(data, index)
        elif choice == "4":
            index = int(input("Enter the index of the recipe: ")) - 1
            update_recipe(data, index)
        elif choice == "5":
            index = int(input("Enter the index of the recipe: ")) - 1
            delete_recipe(data, index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
