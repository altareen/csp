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




