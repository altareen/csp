# Exercise 2, page 124
weekdays = {}
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        day = line[2]
        if day not in weekdays:
            weekdays[day] = 1
        else:
            qty = weekdays[day]
            weekdays[day] = qty + 1
print(weekdays)


