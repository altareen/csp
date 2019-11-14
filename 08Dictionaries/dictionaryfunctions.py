# create a dictionary that contains fruit
fruit = {"pear":2, "banana":3, "orange":5}

# using sorted() to get a list of sorted keys
ranked = sorted(fruit)
print(ranked)

# using keys() to generate a list of the keys
produce = fruit.keys()
produce = list(produce)
print(produce)

# using copy() to create a distinct clone of the dictionary
citrus = fruit.copy()
print(citrus)

# using values() to generate a list of values
quantity = fruit.values()
quantity = list(quantity)
print(quantity)

#using items() to generate a list of key-value pairs
inventory = fruit.items()
inventory = list(inventory)
print(inventory)








