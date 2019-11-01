# the range() function

# generate a list from 0 to n-1
result = range(5)
result = list(result)
print(result)

# generate a list from m to n-1
result = range(2, 7)
result = list(result)
print(result)

# generate a list whose integers are separated by
# gaps larger than 1.
result = range(2, 15, 3)
result = list(result)
print(result)

result = range(9, 2, -1)
result = list(result)
print(result)

# using range() with a for loop
for item in range(82, 37, -5):
    print(item)

# the append() method
sports = ["basketball", "football"]
sports.append("badminton")
print(sports)

temps = []
temps.append(47)
temps.append(52)
temps.append(58)
temps.append(63)
temps.append(68)
print(temps)

# the extend() method
notes = ["do", "ray", "mi"]
melody = ["fa", "so", "la"]
notes.extend(melody)
print(notes)













