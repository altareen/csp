# using the index() method
breakfast = ["eggs", "juice", "toast"]
breakfast.insert(1, "bacon")
print(breakfast)

scores = [98, 21, 34, 63, 28, 94]
scores.insert(0, 32)
print(scores)

# sorting elements from low to high
expenses = [29, 38, 47, 32, 98, 43]
expenses.sort()
print(expenses)

# sorting elements from high to low
temps = [29, 83, 47, 23, 98, 41]
temps.sort(reverse=True)
print(temps)

# sorting a list of strings
animals = ["camel", "bear", "goat", "dolphin"]
animals.sort()
print(animals)

# reversing the elements of a list
meals = ["breakfast", "lunch", "dinner"]
meals.reverse()
print(meals)

outcomes = [12, 90, 38, 74, 29, 83, 79, 28]
outcomes.reverse()
print(outcomes)

# removing an element from a list
snacks = ["pizza", "wings", "soda", "chips"]
snacks.remove("soda")
print(snacks)

outputs = [12, 90, 38, 47, 90, 13, 22, 90, 75]
outputs.remove(90)
print(outputs)
