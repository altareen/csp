# using the list function
lunch = "pizza"
letters = list(lunch)
print(letters)

# using the split method to create a list of words
meal = "I like hamburgers"
words = meal.split()
print(words)

# using split on a comma separated string
prices = "92,37,42,93,87,42"
stock = prices.split(",")
print(stock)

# using split with a colon delimiter
coords = "90:33:47:98:34:27:43:98"
gps = coords.split(":")
print(gps)

# using join to create a comma separated string
roster = ["alice", "bob", "carl", "dan"]
delimiter = ","
students = delimiter.join(roster)
print(students)

# creating a clone of a list
menu = ["rice", "noodles", "beef"]
specials = menu[:]

# aliasing: do not use this method to copy a list
food = menu

menu.append("chicken")

print("menu: " + str(menu))
print("specials: " + str(specials))
print("food: " + str(food))










