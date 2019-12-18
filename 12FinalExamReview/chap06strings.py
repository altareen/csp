# Chapter 6: Strings Exercises

# Question 1.
def wordstats(phrase):
    print(len(phrase))
    print(phrase*10)
    print(phrase[0])
    print(phrase[:3])
    print(phrase[-3:])
    print(phrase[::-1])
    print(phrase[6])
    print(phrase[1:-1])
    print(phrase.upper())
    print(phrase.replace("p", "d"))


wordstats("pepperoni")
#wordstats("pizza")

# Question 2.
def estimatewords(phrase):
    num = phrase.count(" ")
    return num

result = estimatewords("Soft, what light through yonder window breaks.")
print(result)

# Question 3.
def balancedparentheses(equation):
    result = False
    open = equation.count("(")
    closed = equation.count(")")
    if open == closed:
        result = True
    else:
        result = False
    return result

result = balancedparentheses("((x+y))))")
print(result)

# Question 4.
def containsvowels(word):
    for letter in word:
        if letter in "aeiou":
            return True
    return False

result = containsvowels("cauliflower")
print(result)

result = containsvowels("glrph")
print(result)

# Question 5.
def alterstring(word):
    outcome = word[0] + "*" + word[2:] + "!!!"
    return outcome

result = alterstring("pizza")
print(result)

# Question 6.
def parsestring(phrase):
    outcome = phrase.lower()
    outcome = outcome.replace(",", "")
    outcome = outcome.replace(".", "")
    return outcome

result = parsestring("It is the East, and Juliet, is the Sun.")
print(result)

# Question 7.
def palindrome(phrase):
    outcome = False
    backwards = ""
    # Generate the backwards version using a loop
    for letter in phrase:
        backwards = letter + backwards
    # Generate the backwards version with a slice
    backwards = phrase[::-1]
    if phrase == backwards:
        outcome = True
    else:
        outcome = False
    return outcome

result = palindrome("racecar")
print(result)

result = palindrome("pizza")
print(result)

# Question 8.
def determinestudent(roster):
    for person in roster:
        if person.find("prof") != -1:
            return "There is at least one professor in the roster"
    return "The roster only contains students"

result = determinestudent(["alice@student.college.edu", "bob@student.college.edu", "carl@student.college.edu"])
print(result)

result = determinestudent(["aggy@prof.college.edu", "bob@student.college.edu", "carl@student.college.edu"])
print(result)

# Question 9.
def diagonaldigits(num):
    for item in range(num):
        outcome = item*" " + str(item+1)
        print(outcome)

diagonaldigits(4)

# Question 10.
def doubledletters(word):
    for letter in word:
        print(letter*3)

doubledletters("cake")

# Question 11.
def splitstring(word):
    pos = word.find("a")
    print(word[:pos+1])
    print(word[pos+1:])

splitstring("buffalo")

# Section 3

# Question 12.
def otheruppercase(word):
    outcome = ""
    for i in range(len(word)):
        if i%2 == 0:
            outcome += word[i]
        else:
            outcome += word[i].upper()
    return outcome

result = otheruppercase("rhinoceros")
print(result)

# Question 13.
def blendwords(one, two):
    outcome = ""
    for i in range(len(one)):
        combine = one[i] + two[i]
        outcome += combine
    return outcome

result = blendwords("abcde", "ABCDE")
print(result)

# Question 14.
def makeupper(name):
    outcome = ""
    line = name.split()
    for i in range(len(line)):
        line[i] = line[i].capitalize()
    outcome = " ".join(line)
    return outcome

result = makeupper("sherlock benedict holmes")
print(result)

# Question 17.
def generateletters():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alpha)):
        result = alpha[i:] + alpha[:i]
        print(result)

generateletters()




