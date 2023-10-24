from recipes import load_recipes as load, save_recipes as save
import sys
import os
import subprocess
import shutil

FOLDER = os.path.abspath(os.path.dirname(sys.argv[0]))
FILE = os.path.join(FOLDER, "recipes.json")

CLS = lambda: os.system("cls") if sys.platform == "nt" else os.system("clear")


def choose_recipe():
    recipes = load()
    while True:
        CLS()
        print("**************************")
        print("****  Recipe Manager  ****")
        print("**************************")
        print("")
        for index, recipe in enumerate(recipes["recipes"]):
            print(f"{index+1}.", recipe["name"])
            print("\t" + recipe["desc"])
        choice = ""
        while not choice:
            choice = input("Type your choice and press Enter: ")
        choice = choice.strip().lower()
        if choice.isdigit():
            new_recipe()


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


def new_recipe():
    CLS()
    print("************************")
    print("*****  New Recipe  *****")
    print("************************")
    print("")
    recipe={}
    name=''
    while not name:
        name = input("Type the recipe name, and press Enter: ")
        name = name.strip()
    recipe["name"]=name
    desc=''
    while not desc:
        desc = input("Type the recipe description, and press Enter: ")
        desc = desc.strip()
    recipe["desc"]=desc


def edit_recipe():
    CLS()
    print("*************************")
    print("*****  Edit Recipe  *****")
    print("*************************")
    print("")
    recipe = choose_recipe()


def main():
    CLS()
    print("**************************")
    print("****  Recipe Manager  ****")
    print("**************************")
    print("")
    while True:
        print("n: new recipe")
        print("e: edit recipe")
        print("d: delete recipe")
        print("q: quit program")
        choice = ""
        while not choice:
            choice = input("Type your choice and press Enter: ")
        choice = choice.strip().lower()
        if choice == "n":
            new_recipe()
        elif choice == "e":
            edit_recipe()
        elif choice == "d":
            delete_recipe()
        elif choice == "q":
            sys.exit()

        print("")


main()
