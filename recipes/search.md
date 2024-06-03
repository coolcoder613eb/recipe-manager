<title>Recipes</title>
<script>
function main(){
const files=[['Cheese-Cake.html', '<ul>\n<li><strong><a href="Cheese-Cake.html">Cheese Cake</a></strong><br />\nA delicous cheesecake.</li>\n</ul>', '<title>Cheese Cake</title>\n# Cheese Cake\nA delicous cheesecake.  \n## Base\n### Ingredients\n- 100gm marg  \n- 1/2 cup sugar  \n- 1 1/2 cup flour  \n- 1/2 tsp baking powder  \n- pinch salt  \n- 1 egg  \n### Instructions\nPress into dish and bake 15/20 min at 180 °C  \n## Cheese\n### Ingredients\n- 1 kilo quarg (cream cheese)  \n- 1 sour cream - 300ml  \n- 3/4 package vanilla pudding  \n- 1 cup sugar  \n- 4 eggs  \n### Instructions\nMix by hand,  \npour onto base, or biscuits with marg,  \nand bake 1hr at 180 °C  \n'], ['Pancakes.html', '<ul>\n<li><strong><a href="Pancakes.html">Pancakes</a></strong><br />\nPancakes, great for breakfast.</li>\n</ul>', '<title>Pancakes</title>\n# Pancakes\nPancakes, great for breakfast.  \n## Ingredients\n- 5 eggs  \n- 1/2 cup milk  \n- 6 tbs flour (plenty!)  \n- 2 tbs sugar  \n## Instructions\nMix and fry.  \n']];
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
recipes.innerHTML=matchArr.join("\n");
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

- **[Cheese Cake](Cheese-Cake.html)**  
A delicous cheesecake.
- **[Pancakes](Pancakes.html)**  
Pancakes, great for breakfast.
</div>
* * *

</body>
