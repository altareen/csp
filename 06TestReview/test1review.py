# Fall 2015 Test 1

# Question 16.
num = 10
num = num + num
num = num - 5
print(num)

# Question 17.
x = min(max(13, 7), 9)
print(x)

# Question 18.
pancakes = 10
if pancakes > 3:
    print("Yum!")
else:
    print("Still hungry!")

# Question 19.
age = 16
if age >= 18:
    print("You can drive")
elif age < 0:
    print("You are a time traveller")
else:
    print("Too young to drive")

# Question 20.
def circlearea(radius):
    result = 3.14 * radius ** 2
    return result

outcome = circlearea(5)
print(outcome)

# Question 21.
def totalseconds(hours, minutes, seconds):
    result = 60*60*hours + 60*minutes + seconds
    return result

outcome = totalseconds(7, 21, 37)
print(outcome)

# Question 22.
def countup():
    timeleft = 1
    while timeleft <= 5:
        print("time left:" + str(timeleft))
        timeleft += 1
    print("Blastoff!")

countup()

# Question 24.
def grosspay(hours, rate):
    pay = 0
    if hours <= 40:
        pay = 40*rate
    else:
        pay = 40*rate + (hours-40)*rate*1.5
    return pay

outcome = grosspay(55, 12.75)
print(outcome)


# Fall 2017 Test 1

# Question 34.
x = 25
y = 5
while y <= x:
    y = y + 5

# Question 35.
def countvowels(sample):
    count = 0
    for letter in sample:
        if letter in "aeiou":
            count += 1
    return count

result = countvowels("azcbobobegghakl")
print(result)

# Question 36.
def extraend(word):
    last = word[-2:]
    result = last * 3
    return result

result = extraend("hello")
print(result)

# Question 37.
def piglatin(word):
    result = ""
    first = word[0]
    if first in "aeiou":
        result = word + "hay"
    else:
        result = word[1:] + first + "ay"
    return result

result = piglatin("orange")
print(result)

result = piglatin("peach")
print(result)

# Fall 2018 Test 1

# Programming Question 3.

def multiply(grow, shrink):
    product = 0
    while shrink > 0:
        if shrink%2 == 1:
            product = product + grow
        grow = grow * 2
        shrink = shrink//2
    return product

result = multiply(23, 58)
print(result)

