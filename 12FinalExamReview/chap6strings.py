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
