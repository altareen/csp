# concatenating two strings
candy = "bubble" + "gum"
print(candy)

greetings = "hello" * 3
print(greetings)

# you cannot change a string
grocery = "Mango"
dance = "T" + grocery[1:]
print(dance)

# looping across a string
fruit = "raspberry"
for letter in fruit:
    print(letter)

for item in "cauliflower":
    print(item)

# counting the a's in a string
word = "bananapapaya"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(count)

result = "a" in "banana"
print(result)

outcome = "raw" in "strawberry"
print(outcome)

solution = "pizza" in "hamburger"
print(solution)

snacks = "pizza, wings, burgers"
if "chips" not in snacks:
    print("You forgot the chips!")

