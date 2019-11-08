# converting a string into a list of characters
lunch = "pizza"
letters = list(lunch)
print(letters)

# converting a string into a list of words
meal = "I like hamburgers"
words = meal.split()
print(words)

# placing comma separated data into a list
prices = "12,98,34,23,19,87,45"
stock = prices.split(",")
print(stock)

coords = "21:93:87:41:23:90:84:72:89"
gps = coords.split(":")
print(gps)

# create a string from a list of strings
roster = ["alice", "bob", "carl", "dan"]
delimiter = ","
students = delimiter.join(roster)
print(students)

# making a copy of a list: cloning
menu = ["rice", "noodles", "beef"]
specials = menu[:]
print(specials)

# aliasing: do not copy a list in this manner
food = menu
print(food)

menu.append("chicken")
print("menu: " + str(menu))
print("specials: " +  str(specials))
print("food: " + str(food))
