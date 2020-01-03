# Section 3

# Question 1
def countarticles(text):
    sentence = text.split()
    result = []
    articles = ["a", "an", "the"]
    for word in articles:
        amount = sentence.count(word)
        result.append(amount)
    return result

result = countarticles("the other night, I went to the pizza store and got a large cheese pizza with all the toppings and an ice cream sandwich and a soda from the vending machine.")
print(result)

# Question 2
def separateplus(nums):
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    outcome = "+".join(nums)
    return outcome

result = separateplus([2, 5, 11, 33, 55])
print(result)

# Question 3
def thirdword(text):
    outcome = []
    sentence = text.split()
    print(sentence[2])
    for i in range(len(sentence)):
        if (i+1)%3 == 0:
            outcome.append(sentence[i])
    return outcome

result = thirdword("the other night, I went to the pizza store and got a large cheese pizza with all the toppings and an ice cream sandwich and a soda from the vending machine.")
print(result)

# Question 4
import random
def randomizewords(text):
    sentence = text.split()
    outcome = []
    while len(sentence) > 0:
        word = random.choice(sentence)
        outcome.append(word)
        sentence.remove(word)
    return outcome

result = randomizewords("the other night, I went to the pizza store and got a large cheese pizza with all the toppings and an ice cream sandwich and a soda from the vending machine.")
print(result)

