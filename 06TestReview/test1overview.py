# Fall 2016 Test 1

# Question 16.
num = 11
if num%2 == 0:
    print("even")
else:
    print("odd")

# Question 17.
num = 35
if num%5 == 0 and num%7==0:
    print("multiple of 5 and 7")

# Question 18.
num = 0
while num < 3:
    print(num)
    num += 1

# Question 19.
num = 5
while num < 10:
    print(num)
    num += 2

# Question 20.
for item in range(5):
    print(item)

# Question 21.
for item in range(1, 6):
    print(item)

# Question 22.
def circlearea(radius):
    result = 3.14 * radius ** 2
    return result

outcome = circlearea(5)
print(outcome)

# Question 23.
def totalseconds(hours, minutes, seconds):
    result = 60*60*hours + 60*minutes + seconds
    return result

outcome = totalseconds(7, 21, 37)
print(outcome)

# Question 24.
def temperature(fahrenheit):
    celsius = 5.0/9.0*(fahrenheit-32)
    return celsius

outcome = temperature(100)
print(outcome)

# Question 25.
def grosspay(hours, rate):
    pay = 0
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40*rate + (hours-40)*rate*1.5
    return pay

outcome = grosspay(50, 15.0)
print(outcome)

# Question 26.
def triangle(adj, opp, hyp):
    result = False
    if adj > opp + hyp:
        result = False
    elif opp > adj + hyp:
        result = False
    elif hyp > adj + opp:
        result = False
    else:
        result = True
    return result

outcome = triangle(12, 1, 1)
print(outcome)
outcome = triangle(3, 4, 5)
print(outcome)

# Question 27.
def computegrade(score):
    if score < 0.0 or score > 1.0:
        print("out of range")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

computegrade(787)

num = 8
print(type(num))
value = 8.0
print(type(value))


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
