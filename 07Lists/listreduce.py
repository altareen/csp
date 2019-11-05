# using the pop() method
drinks = ["tea", "coffee", "cookie", "juice"]
pastry = drinks.pop(2)
print(pastry)
print(drinks)

# using del to remove a single element
vegetables = ["celery", "watermelon", "broccoli"]
del vegetables[1]
print(vegetables)

# using del to remove several elements
chemicals = ["Na", "He", "Si", "Ca", "Au", "Pb"]
del chemicals[1:4]
print(chemicals)

# count the number times an element occurs
moves = ["up", "up", "down", "down", "up", "up"]
num = moves.count("up")
print(num)

flavour = ["cheese", "bbq", "salty", "bbq"]
position = flavour.index("bbq")
print(position)
