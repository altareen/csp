# Section 2

# Question 1.
nums = [2,9,38,7,43,29,8,47,65,24,98,65,74]
print(len(nums))
print(nums[12])
print(nums[-1])

# print the list in reverse order using a for loop
outcome = []
for i in range(len(nums)-1,-1,-1):
    outcome.append(nums[i])
print(outcome)

# use slicing to generate a list in reverse order
result = nums[::-1]
print(result)

if 5 in nums:
    print("Yes")
else:
    print("No")

qty = nums.count(5)
print(qty)

del nums[0]
print(nums)
del nums[-1]
print(nums)
nums.sort()
print(nums)

for item in nums:
    if item < 5:
        print(item)

# Question 2.
import random
nums = []
for trial in range(20):
    value = random.randint(1, 100)
    nums.append(value)
print(nums)

average = sum(nums)/len(nums)
print(average)

largest = max(nums)
print(largest)

smallest = min(nums)
print(smallest)

twin = nums[:]
twin.sort()
print(twin)
print(twin[1])
print(twin[-2])

count = 0
for item in nums:
    if item%2 == 0:
        count += 1
print("quantity of even numbers:", count)

# Question 3.
nums = [8, 9, 10]
nums[1] = 17
print(nums)

nums.extend([4, 5, 6])
print(nums)

del nums[0]
print(nums)

nums.sort()
print(nums)

nums.extend(nums[:])
print(nums)

nums.insert(3, 25)
print(nums)

# Question 4.
nums = []
for trial in range(20):
    value = random.randint(1, 12)
    nums.append(value)
print(nums)

for i in range(len(nums)):
    if nums[i] > 10:
        nums[i] = 10
print(nums)

# Question 5.
words = ["Soft", "what", "light", "through", "yonder", "window", "breaks"]
for i in range(len(words)):
    item = words[i]
    words[i] = item[1:]
print(words)


