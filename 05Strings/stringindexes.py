# extracting a single letter from a string
fruit = "watermelon"
first = fruit[0]
print(first)

letter = fruit[5]
print(letter)

letter = "pizza"[1]
print(letter)

last = fruit[9]
print(last)

last = fruit[-1]
print(last)

letter = fruit[-10]
print(letter)

vegetable = "cauliflower"
quantity = len(vegetable)
print(quantity)

last = vegetable[quantity-1]
print(last)

# string slicing
dessert = "chocolate"
drink = dessert[3:7]
print(drink)

breakfast = "pineapple"
tree = breakfast[0:4]
cone = breakfast[:4]
print(tree)
print(cone)

flavor = "strawberry"
snack = flavor[5:10]
food = flavor[5:]
print(snack)
print(food)

icecream = flavor[:]
print(icecream)

