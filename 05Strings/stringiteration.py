# concatenating two strings
candy = "bubble" + "gum"
print(candy)

# duplicating strings
greetings = "hello" * 3
print(greetings)

grocery = "Mango"
dance = "T" + grocery[1:]
print(dance)

# looping across a string
fruit = "raspberry"
for letter in fruit:
    print(letter)

for item in "cauliflower":
    print(item)

# counting items in a string
word = "bananapapaya"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(count)

# the in operator
result = "a" in "banana"
print(result)

outcome = "raw" in "strawberry"
print(outcome)

solution = "soda" in "hamburger"
print(solution)

# the not in operator
snacks = "pizza, wings, burgers"
if "chips" not in snacks:
    print("You forgot the chips!")










