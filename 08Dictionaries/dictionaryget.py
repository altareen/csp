fruit = {"pear":2, "banana":3, "orange":5}

# using get() to retrieve a value from fruit
result = fruit.get("orange", 0)
print(result)

# using get() when the key is absent from fruit
result = fruit.get("watermelon", 0)
print(result)

# looping across a dictionary
for key in fruit:
    print(key)

# looping across a dictionary and looking up values
for key in fruit:
    print(fruit[key])

for key in fruit:
    print(fruit.get(key, 0))

for value in fruit.values():
    print(value)

# Python for Everybody, Exercise 2, page 124
weekdays = {}
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        day = line[2]
        weekdays[day] = weekdays.get(day, 0) + 1
print(weekdays)

# Python for Everybody, Exercise 3, page 124
emails = {}
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        address = line[1]
        emails[address] = emails.get(address, 0) + 1
print(emails)














