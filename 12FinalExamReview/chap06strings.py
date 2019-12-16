# Chapter 6: Strings Exercises

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

def estimatewords(phrase):
    num = phrase.count(" ")
    return num

result = estimatewords("Soft, what light through yonder window breaks.")
print(result)


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


