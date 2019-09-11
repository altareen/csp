# using the and operator
a = False
b = True
print(a and b)

# using the or operator
c = True
d = False
print(c or d)

# using the not operator
e = True
print(not e)

# a complicated boolean expression
result = (a or e) and ((c or d) or (not b) and c)
print(result)

# blending the comparison and logic operators
chips = 34
soda = 65
if chips > 0 and soda > 0:
    print("You have snacks.")

money = 933
creditcard = False
if (money > 1000) or (creditcard == True):
    print("You can buy an iPhone.")
