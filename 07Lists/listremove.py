# using the pop() method
drinks = ["tea", "coffee", "cookie", "juice"]
pastry = drinks.pop(2)
print(pastry)
print(drinks)

# using the del operator
vegetables = ["celery", "watermelon", "broccoli"]
del vegetables[1]
print(vegetables)

# using del to remove several elements
chemicals = ["Na", "He", "Si", "Ca", "Au", "Pb"]
del chemicals[1:4]
print(chemicals)

# using the count() method
moves = ["up", "up", "down", "down", "up", "up"]
num = moves.count("up")
print(num)

# using the index() method
flavour = ["cheese", "bbq", "salty", "bbq"]
position = flavour.index("bbq")
print(position)


