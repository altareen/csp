# creating an empty dictionary
sports = {}
print(sports)

# creating a dictionary with key-value pairs
fruit = {"pear":2, "banana":3, "orange":5}
print(fruit)

# looking up a value from a dictionary
value = fruit["orange"]
print(value)

# using len() to determine the number of key-value pairs
total = len(fruit)
print(total)

# determining if a key exists in a dictionary with: in
result = "banana" in fruit
print(result)

outcome = "kiwi" in fruit
print(outcome)

# remove a key-value pair from fruit
del fruit["pear"]
print(fruit)

# adding a key-value pair to the dictionary
fruit["mango"] = 8
print(fruit)

