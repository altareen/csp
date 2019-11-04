# the range(n) function
result = range(5)
result = list(result)
print(result)

# the range(m, n) function
result = range(2, 7)
result = list(result)
print(result)

# the range(m, n, step) function
result = range(2, 15, 3)
result = list(result)
print(result)

# using a negative step integer
result = range(9, 2, -1)
result = list(result)
print(result)

# using the range() function with a loop
for item in range(23, 98, 9):
    print(item)

# using the append() function
sports = ["basketball", "football"]
sports.append("badminton")
print(sports)

temps = []
temps.append(47)
temps.append(53)
temps.append(57)
temps.append(61)
temps.append(65)
temps.append(68)
temps.append(73)
temps.append(76)
print(temps)

# using the extend() method
notes = ["do", "ray", "mi"]
melody = ["fa", "so", "la"]
notes.extend(melody)
print(notes)

