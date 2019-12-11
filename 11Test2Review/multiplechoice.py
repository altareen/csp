# Mulitple Choice

# 1.
friends = ["Joseph", "Glenn", "Sally"]
print(friends[2])

# 2.
fruit = ["banana", "mango", "kiwi"]
print(len(fruit))

# 3.
num = list(range(5))
print(num)

# 4.
first = [1, 2, 3]
second = [4, 5, 6]
nums = first + second
print(len(nums))

# 5.
nums = [9, 41, 12, 3, 74, 15]
print(nums[2:4])


# 6.
nums = [29, 93, 82]
nums.append(34)
print(nums)

# 7.
friends = ["Joseph", "Glenn", "Sally"]
friends.sort()
print(friends)

# 8.
person = friends.pop()
print(person)
print(friends)

# 9.
breakfast = "eggs toast bacon juice"
food = breakfast.split()
print(food)

# 10.
for num in range(1, 10, 2):
    print(num)

# 11.
lunch = {"pizza":10, "burger":12}
food = lunch.get("chips", 0)
print(food)

# 13.
#fruit = {"banana":5, "pear":3, "orange":8}
#result = fruit["kiwi"]
# Fails with a Traceback.

# 14.
fruit = {"banana":5, "pear":3, "orange":8}
result = fruit.get("kiwi", 0)
print(result)

# 15.
fruit = {"banana":5, "pear":3, "orange":8}
for item in fruit:
    print(item)

# 17.
fruit = {"banana":5, "pear":3, "orange":8}
del fruit["orange"]
print(fruit)

# 18.
drinks = {"coffee":87, "tea":23, "juice":49}
result = list(drinks.values())
print(result)

# 19.
fruit = {"banana":5, "pear":3, "orange":8}
fruit["orange"] -= 2
print(fruit)

# 20.
cheese = {"swiss":3, "cheddar":7, "gouda":6}
result = "swiss" in cheese
print(result)

# Short Answer

# 1.
cheeses = ["Cheddar", "Edam", "Gouda"]
print(cheeses[0])

# 2.
# [0, 0, 0, 0]
print([0] * 4)

# 3.
#["pizza", "burger", "fries"]
snacks = ["pizza", "burger"]
snacks.append("fries")
print(snacks)

# 4.
drinks = ["tea", "soda", "cola", "juice"]
drinks.sort()
print(drinks)

# 5.
dinner = ["salad", "bread", "steak", "potato"]
del dinner[1]
print(dinner)

# 6.
nums = [3, 41, 12, 9, 74, 15]
print(max(nums))

# 7.
food = {"pizza":3}
food["fries"] = 10
print(food)

# 8
treasure = {"gold":50, "silver":100}
print("gold" in treasure)

# 9.
inventory = {
    "pocket":"lint",
    "canteen":"water",
    "pouch":"flint",
    "backpack":["shovel", "bedroll", "rope"]
}
print(inventory["backpack"])

# 10.
fortune = {"gold":500}
fortune["gold"] += 50
print(fortune)

# 11.
inventory = {
    "gold":500,
    "backpack":["xylophone", "dagger", "bedroll"]
}
inventory["backpack"].sort()
print(inventory["backpack"])
print(inventory)

# 12.
grocery = {"kiwi":5, "grape":12}
del grocery["kiwi"]
print(grocery)

# 13.
salad = {"caesar":1, "garden":2}
salad["vegetable"] = 3
print(salad)

# 14.
singer = {"justin":"bieber", "taylor":"swift", "ed":"sheeran"}
print(singer.get("swift", "guitar"))

# 15.
sports = {"tennis":43, "football":78, "badminton":52}
result = list(sports.keys())
print(result)

# Part 3: Python Programming

# Question 1.
def inventory():
    '''
    returns a float, the total value of all the products.
    '''
    prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}
    stock = {"banana":6, "apple":7, "orange":31, "pear":15}
    # YOUR CODE HERE
    total = 0
    for item in prices:
        product = prices[item] * stock[item]
        total += product
    return total

result = inventory()
print(result)

# Question 2.
def transcription(dna):
    mapping = {"A": "U", "C": "G", "G": "C", "T": "A"}
    rna = ""
    for letter in dna:
        codon = mapping[letter]
        rna += codon
    return rna

result = transcription("AGGCTACGT")
print(result)

# Question 3.
def convertmandarin(eng):
    nums = {"0": "ling", "1": "yi", "2": "er", "3": "san", "4": "si", "5": "wu", "6": "liu", "7": "qi", "8": "ba", "9": "jiu", "10": "shi"}
    result = ""
    value = int(eng)
    if 0 <= value <= 9:
        result = nums[eng]
    elif 10 <= value <= 19:
        digit = eng[1]
        result = "shi" + " " + nums[digit]
    elif 20 <= value <= 99:
        first = eng[0]
        second = eng[1]
        if second == "0":
            result = nums[first] + " shi"
        else:
            result = nums[first] + " shi " + nums[second]
    return result

result = convertmandarin("3")
print(result)
result = convertmandarin("16")
print(result)
result = convertmandarin("36")
print(result)
result = convertmandarin("20")
print(result)





