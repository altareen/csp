def pythagoras(opp, adj, tau, epsilon):
    hyp = (opp**2 + adj**2)**0.5
    solution = hyp * tau + epsilon
    return solution

result = pythagoras(3.2, 4.7, 1.3, 0.57)
print(result)

# a function that takes no parameters and does not return a value
def displayhello():
    print("hello")

displayhello()

# a function that takes parameters and does not return a value
def displaygoodbye(note):
    print("Message: "+ note)

displaygoodbye("See you later.")

# a function that takes no parameters and returns a value
def greetings():
    output = "have a nice day."
    return output

result = greetings()
print(result)

# a function that takes parameters and returns a value
def farewell(note, repeat):
    outcome = note * repeat
    return outcome

result = farewell("Take care.", 5)
print(result)

