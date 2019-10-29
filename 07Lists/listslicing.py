# list slicing
lunch = ["soup", "salad", "rice", "beans"]
print(lunch[1:3])

# changing multiple elements with a list slice
lunch[1:3] = ["fries", "noodles"]
print(lunch)

# looping with a for-each loop
snacks = ["chips", "cake", "banana"]
for item in snacks:
    print(item)

# looping across a list, while making changes
primes = [11, 13, 17, 19, 23]
for i in range(len(primes)):
    primes[i] = primes[i] * 2
print(primes)

# using + to concatenate two lists
food = ["chicken", "beef", "fish"]
supplies = ["soap", "detergent", "napkins"]
groceries = food + supplies
print(groceries)

# repeating a list with the * operator
result = [5, 8] * 3
print(result)

dataset = [0] * 20
print(dataset)








