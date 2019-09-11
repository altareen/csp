# sample boolean values with: and
a = True
b = False
print(a and b)

# sample boolean values with: or
c = False
d = True
print(c or d)

# sample boolean value with: not
e = True
print(not e)

# create a complicated boolean expression
result = (a and d) or not(c or a) and not c
print(result)

# combining comparison and boolean
chips = 92
soda = 87
if (chips > 0 and soda > 0):
    print("You have snacks.")

# using the or operator
money = 874
creditcard = True
if (money > 1000 or creditcard == True):
    print("You can buy an iPhone.")
