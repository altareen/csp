# Chapter 6: Strings Exercises

# Question 1
def wordstats(phrase):
    print(len(phrase))
    print(phrase*10)
    print(phrase[0])
    print(phrase[:3])
    print(phrase[-3:])
    result = ""
    for letter in phrase:
        result = letter + result
    print(result)
    print(phrase[::-1])
    print(phrase[6])
    print(phrase[1:-1])
    print(phrase.upper())
    print(phrase.replace("p", "q"))

wordstats("pepperoni")

# Question 2.
def estimatewords(phrase):
    num = phrase.count(" ")
    return num

result = estimatewords("Soft, what light through yonder window breaks.")
print(result)

# Question 3.
def balancedparentheses(equation):
    open = equation.count("(")
    closed = equation.count(")")
    if open == closed:
        return True
    else:
        return False

result = balancedparentheses("((x+y)))))")
print(result)

# Question 4.
def containsvowels(phrase):
    for letter in phrase:
        if letter in "aeiou":
            return True
    return False

result = containsvowels("orange")
print(result)

result = containsvowels("glrph")
print(result)

# Question 5.
def buildalternate(phrase):
    outcome = phrase[0] + "*" + phrase[2:] + "!!!"
    return outcome

result = buildalternate("pizza")
print(result)

# Question 6.
def parseword(phrase):
    solution = phrase.lower()
    solution = solution.replace(",", "")
    solution = solution.replace(".", "")
    return solution

result = parseword("It is the East, and, Juliet is the Sun.")
print(result)

# Question 7.
def palindrome(phrase):
    result = False
    backwards = ""
    # first method of producing a backwards string
    for letter in phrase:
        backwards = letter + backwards
    # the hack method of producing a backwards string
    backwards = phrase[::-1]
    if phrase == backwards:
        result = True
    else:
        result = False
    return result

result = palindrome("amanaplanacanalpanama")
print(result)

result = palindrome("pizza")
print(result)

# Question 8.
def checkaddresses(roster):
    result = ""
    for person in roster:
        if person.find("prof") != -1:
            return "There is at least one professor in the roster."
    result = "The roster contains all students"
    return result

result = checkaddresses(["alice@student.college.edu", "bob@student.college.edu", "carl@student.college.edu"])
print(result)

result = checkaddresses(["aggy@prof.college.edu", "bob@student.college.edu", "carl@student.college.edu"])
print(result)

# Question 9.
def diagonaldigits(num):
    for item in range(num):
        output = " "*item + str(item+1)
        print(output)

diagonaldigits(4)

# Question 10.
def doubleletters(word):
    for letter in word:
        print(letter*3)

doubleletters("cake")

# Question 11.
def splitstring(word):
    pos = word.find("a")
    print(word[:pos+1])
    print(word[pos+1:])

splitstring("buffalo")

# Question 12.
def othercaps(word):
    result = ""
    for i in range(len(word)):
        if i%2 == 0:
            result += word[i:i+1]
        else:
            result += word[i:i+1].upper()
    return result

result = othercaps("rhinoceros")
print(result)

# Section 2

# Question 13.
def blendedwords(one, two):
    outcome = ""
    for i in range(len(one)):
        combined = one[i] + two[i]
        outcome += combined
    return outcome

result = blendedwords("abcde", "ABCDE")
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
def wrapalphabet():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alpha)):
        print(alpha[i:] + alpha[:i])

wrapalphabet()

# Question 21.
import random
def anagram(word):
    outcome = ""
    text = list(word)
    while len(text) > 0:
        letter = random.choice(text)
        outcome += letter
        text.remove(letter)
    return outcome

result = anagram("idle")
print(result)
