from ete3 import Tree 

t = Tree('covid_tree.nhx') 
t.render("mytree.png", w=183, units="mm")