# Section 2

# Question 1
def countarticles(text):
    sentence = text.split()
    outcome = []
    articles = ["a", "an", "the"]
    for word in articles:
        amount = sentence.count(word)
        outcome.append(amount)
    return outcome

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
    for i in range(len(sentence)):
        if (i+1)%3 == 0:
            outcome.append(sentence[i])
    return outcome

result = thirdword("the other night, I went to the pizza store and got a large cheese pizza with all the toppings and an ice cream sandwich and a soda from the vending machine.")
print(result)

# Question 4
import random
def rearrangewords(text):
    sentence = text.split()
    random.shuffle(sentence)
    return sentence

result = rearrangewords("the other night, I went to the pizza store and got a large cheese pizza with all the toppings and an ice cream sandwich and a soda from the vending machine.")
print(result)

# Question 6
def lotterydrawing():
    result = []
    nums = list(range(1, 49))
    for trial in range(6):
        pick = random.choice(nums)
        result.append(pick)
        nums.remove(pick)
    return result

result = lotterydrawing()
print(result)



