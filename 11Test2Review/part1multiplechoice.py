# Fall 2018 Test 2: Lists and Dictionaries

# 1.
friends = ["Joseph", "Glenn", "Sally"]
print(friends[2])

# 2.
fruit = ["kiwi", "mango", "orange"]
print(len(fruit))

# 3.
nums = list(range(5))
print(nums)

# 4.
first = [1, 2, 3]
second = [4, 5, 6]
nums = first + second
print(len(nums))

# 5.
nums = [9, 41, 12, 3, 74, 15]
print(nums[2:4])

# 6.
nums = [20, 39, 83]
nums.append(43)
print(nums)

# 7.
friends = ["Joseph", "Glenn", "Sally"]
friends.sort()
print(friends[0])

# 8.
nums = [29, 38, 74, 32, 98]
result = nums.pop()
print(result)
print(nums)

# 9.
breakfast = "eggs bacon toast juice"
food = breakfast.split()
print(food)

# 10.
for num in range(1, 10, 2):
    print(num)

lunch = {"pizza":10, "burger":12}
snack = lunch.get("chips", 0)
print(snack)

# 13.
fruit = {"banana":5, "pear":3, "orange":8}
#result = fruit["kiwi"]
print(result)

# 14.
fruit = {"banana":5, "pear":3, "orange":8}
result = fruit.get("kiwi", 0)
print(result)

# 15.
fruit = {"banana":5, "pear":3, "orange":8}
for item in fruit:
    print(item)

# 16.
groceries = fruit.copy()
print(groceries)

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
"Cheddar"

# 2.
#[0, 0, 0, 0]
print([0] * 4)

# 3.
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

# 8.
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
