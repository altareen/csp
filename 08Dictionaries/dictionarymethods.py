# using the sorted() method to produce a list of keys
fruit = {"pear":2, "banana":3, "orange":5}
ranked = sorted(fruit)
print(ranked)

# using the keys() method to produce a list of keys
produce = fruit.keys()
produce = list(produce)
print(produce)

# producing an exact, distinct clone of a dictionary
citrus = fruit.copy()
print(citrus)

# using the values() method to produce a list of values
quantity = fruit.values()
quantity = list(quantity)
print(quantity)

# producing a list consisting of all the key-value pairs
inventory = fruit.items()
inventory = list(inventory)
print(inventory)


