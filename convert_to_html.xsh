for x in g`./recipes/*.md`:
    markdown_py -f @(x.removesuffix('.md')+'.html') @(x) 
