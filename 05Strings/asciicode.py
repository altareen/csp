# convert from a symbol to an ASCII number
numcode = ord("P")
print(numcode)

# convert from ASCII to a symbol
letter = chr(105)
print(letter)

# using the equality operator with strings
password = "basketball"
if password == "basketball":
    print("login successful")

# digits come before lowercase letters
if "999" < "thousand":
    print("access granted")

# uppercase letters come before lowercase
if "PIZZA" < "burger":
    print("dinner time")

num = len("pizza")
print(num)

# using the capitalize method
dinner = "pizza"
result = dinner.capitalize()
print(result)

# applying the lower() method
lunch = "CHEESEburger"
result = lunch.lower()
print(result)

# puts all the letters into uppercase
fruit = "strawberry"
result = fruit.upper()
print(result)

# check that all characters are letters
vegetable = "cauliflower"
result = vegetable.isalpha()
print(result)

dessert = "423chocolates"
result = dessert.isalpha()
print(result)

# check that all characters are numbers
meter = "29387392"
result = meter.isdigit()
print(result)

drink = "58waters"
result = drink.isdigit()
print(result)

# remove whitespace from a string
beverage = "        coffee\n\n\n\n"
result = beverage.strip()
print(result)

# remove whitespace from the right hand side
soda = "sprite\n\n\n\n\n\n\n\n\n\n\n"
result = soda.rstrip()
print(result)

# find a substring within another string
candy = "chocolate"
location = candy.find("cola")
print(location)

location = candy.find("pizza")
print(location)

pastry = "jampieapplepiekiwipieraspberrypie"
location = pastry.find("pie", 13)
print(location)

dinner = "beefstewandburgerswithsalad"
result = dinner.replace("burgers", "pizza")
print(result)

bakery = "strawberryjamorangejamkiwijam"
result = bakery.count("jam")
print(result)

menu = "pizzaburgersfriessoda"
result = menu.startswith("pizza")
print(result)

greetings = "hello\n\n\n\n\nworld\n\n\n"
print(greetings)
