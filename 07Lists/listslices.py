# extracting a slice from a list
lunch = ["soup", "salad", "rice", "beans"]
print(lunch[1:3])

# update the elements in a list
lunch[1:3] = ["fries", "noodles"]
print(lunch)

# looping across a list with a for-each loop
snacks = ["chips", "cake", "banana"]
for item in snacks:
    print(item)

# The range() method
print(list(range(5)))

# looping across a list and making changes
primes = [11, 13, 17, 19, 23]
for i in range(len(primes)):
    primes[i] = primes[i] * 2
print(primes)

# using the concatenation operator: +
food = ["chicken", "beef", "fish"]
supplies = ["soap", "detergent", "napkins"]
grocery = food + supplies
print(grocery)

# using the multiplication operator: *
result = [5, 8] * 3
print(result)

dataset = [0] * 20
print(dataset)

nums = [92, 37, 42, 89]
nums.remove(37)
print(nums)

