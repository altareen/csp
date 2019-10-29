# create a list called fruit
fruit = ["strawberry", 58, 3.5]
print(fruit)

# extract each element from the fruit list
print(fruit[0])
print(fruit[1])
print(fruit[2])

# change values in a list
fruit[1] = 65
print(fruit[1])
print(fruit)

# get the last element in the list
final = fruit[-1]
print(final)

# determine the number of elements in a list
scores = [39, 20, 48, 75, 43]
print(len(scores))

# determine if an element exists in a list
drinks = ["tea", "juice", "soda"]
print("coffee" in drinks)
print("soda" in drinks)

# sorting a list from low to high
scores.sort()
print(scores)

nums = [1, 2, 3]
nums.pop(0)
print(nums)
