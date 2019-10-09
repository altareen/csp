# an example of a for loop
for count in [0, 1, 2, 3, 4]:
    print(count)

nums = [0, 1, 2, 3, 4, 5, 6]
for item in nums:
    print(item)

# summing a sequence of integers
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for item in elements:
    total += item
print(total)

# the range function
sequence = list(range(20))
print(sequence)

# sum all the integers up to 100
outcome = 0
hundred = range(101)
for num in hundred:
    outcome += num
print(outcome)

# using the break statement
import random
while True:
    num = random.randint(1, 10)
    print(num)
    if num == 8:
        break

# using the continue statement
for num in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
    if num == 4:
        continue
    print(num)




