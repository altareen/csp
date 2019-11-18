fruit = {"pear":2, "banana":3, "orange":5}

# using the get() method to retrieve a value
# when the key is in the dictionary
result = fruit.get("orange", 0)
print(result)

# using the get() method when the key is absent
result = fruit.get("watermelon", 0)
print(result)

# loop across the keys in a dictionary
for key in fruit:
    print(key)

# getting the values from a dictionary
for key in fruit:
    print(fruit[key])

# retrieving the values by using the get() method
for key in fruit:
    print(fruit.get(key, 0))

# looping across the values in a dictionary
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
    if line.startswith("From:"):
        line = line.split()
        address = line[1]
        emails[address] = emails.get(address, 0) + 1
print(emails)














