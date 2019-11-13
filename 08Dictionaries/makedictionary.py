# creating an empty dictionary
sports = {}
print(sports)

# creating a dictionary with some initial key-value pairs
fruit = {"pear":2, "banana":3, "orange":5}
value = fruit["orange"]
print(value)

phonebook = {"alice":9283, "bob":8237, "carl":3346}
number = phonebook["bob"]
print(number)

# adding a new key-value pair to the fruit dictionary
fruit["mango"] = 12
print(fruit)

# adding a new key-value pair to the phonebook dictionary
phonebook["dan"] = 1276
print(phonebook)

# using len() to determine the number of key-value pairs
total = len(fruit)
print(total)

# determine if a key exists in a dictionary with: in
result = "banana" in fruit
print(result)

outcome = "kiwi" in fruit
print(outcome)

# using del to remove a key-value pair
del fruit["pear"]
print(fruit)

# adding a key-value pair to a dictionary
fruit["watermelon"] = 15
print(fruit)












