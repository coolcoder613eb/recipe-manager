from export import export_markdown
import os

FOLDER = "./recipes"

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)

for name, text in export_markdown().items():
    with open(
        os.path.join(
            FOLDER, name.replace(" ", "-").replace(".", "-").replace("/", "-") + ".md"
        ),
        "w",
    ) as f:
        f.write(text)
