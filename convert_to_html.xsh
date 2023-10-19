import os
FOLDER = "./recipes/html"

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)
for x in g`./recipes/*.md`:
    markdown_py -f @(x.replace('./recipes/','./recipes/html/').removesuffix('.md')+'.html') @(x) 
