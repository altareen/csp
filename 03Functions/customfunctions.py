def pythagoras(opp, adj, val, epsilon):
    hyp = (opp**2 + adj**2)**0.5
    solution = hyp + val * epsilon
    return solution

result = pythagoras(5.2, 3.4, 2.9, 8.1)
print(result)

def coffeetime(hour, minute):
    if hour == 10:
        return "drink coffee"
    elif minute == 32:
        return "don't drink coffee"
    else:
        return "think about coffee"

result = coffeetime(12, 32)
print(result)

# a function that has no parameters
def displayhello():
    print("hello")

displayhello()

# a function that has parameters
def displaygoodbye(repeat):
    print("bye"*repeat)

displaygoodbye(5)

# a function that takes parameters and does not return a value
def greetings(note, copies):
    print(note * copies)

greetings("hello", 10)

# a function that takes parameters and returns a value
def farewell(notation, quantity):
    output = notation * quantity
    return output

result = farewell("See you later", 8)
print(result)
