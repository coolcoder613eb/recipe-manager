import os
import glob
import shutil
from markdown import markdown

FOLDER = "./recipes/html"
if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)
for filepath in glob.glob("./recipes/*.md"):
    with open(filepath, "r") as file:
        text = file.read()
        html_filename = os.path.join(
            FOLDER, os.path.basename(filepath).replace(".md", ".html")
        )

        with open(html_filename, "w") as html_file:
            html = markdown(text)
            html_file.write(html)
