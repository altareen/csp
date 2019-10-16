# converting a symbol to an ASCII number
numcode = ord("P")
print(numcode)

numcode = ord("h")
print(numcode)

numcode = ord("8")
print(numcode)

# converting an ASCII number to a symbol
initial = chr(84)
print(initial)

initial = chr(105)
print(initial)

initial = chr(55)
print(initial)

# using the equality operator with strings
password = "basketball"
if password == "basketball":
    print("login successful")

# digits come before lowercase
if "999" < "thousand":
    print("access granted")

# uppercase comes before lowercase
if "PIZZA" < "burger":
    print("dinner time")

# the capitalize() method
result = "pizza".capitalize()
print(result)

snack = "cheeseburger"
result = snack.capitalize()
print(result)

fruit = "WATERmelon"
result = fruit.lower()
print(result)

vegetable = "cauliflower"
result = vegetable.upper()
print(result)

# checking if every character is a letter
dinner = "hamburger"
result = dinner.isalpha()
print(result)

dessert = "5chocolatepies!"
result = dessert.isalpha()
print(result)

radius = "923847"
result = radius.isdigit()
print(result)

dinner = "     hamburgers\n\n\n\n\n\n"
result = dinner.strip()
print(result)

lunch = "pizza\n\n\n\n\n\n\n\n\n"
result = lunch.rstrip()
print(result)

candy = "chocolate"
result = candy.find("cola")
print(result)

result = candy.find("soda")
print(result)

pastry = "applepiekiwipiebananapiemangopie"
result = pastry.find("pie", 15)
print(result)

meal = "beefstewwithburgersandsalad"
result = meal.replace("burgers", "pizza")
print(result)

bakery = "strawberryjamorangejammangojam"
result = bakery.count("jam")
print(result)

food = "pizzawithwingsandsoda"
result = food.startswith("pizza")
print(result)

# put carriage returns in your string
greetings = "hello\n\n\n\n\n\nworld\n\n\n\n"
print(greetings)

prose = "She said, \"Hello\" to everyone."
print(prose)

path = "C:\\Documents\\homework\\notes.py"
print(path)

# using the tab character to format tables
print("Product\tWeight\tPrice")
print("kiwi\t0.15kg\t2.95")

# Exercise 6.14
header = "X-DSPAM-Confidence:0.8475"
location = header.find(":")
score = header[location+1:]
score = float(score)
print(location)
print(score)
print(type(score))
















