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
