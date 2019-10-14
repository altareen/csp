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










