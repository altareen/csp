# Section 3

# Question 1.
nums = [2,90,3,18,7,41,2,3,5,9,86,87,5,96,5,76,8]
print(len(nums))

print(nums[16])
print(nums[-1])

# generating a reverse ordered list with a for loop
outcome = []
for i in range(len(nums)-1,-1,-1):
    item = nums[i]
    outcome.append(item)
print(outcome)

# generating a reverse ordered list with a slice
solution = nums[::-1]
print(solution)

if 5 in nums:
    print("Yes")
else:
    print("No")

amount = nums.count(5)
print(amount)

print(nums)

del nums[0]
print(nums)

del nums[-1]
print(nums)

nums.sort()
print(nums)

count = 0
for item in nums:
    if item < 5:
        count += 1
print("items less than 5:", count)

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
print("second smallest:", twin[1])
print("second largest:", twin[-2])

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

nums.pop(0)
print(nums)

nums.sort()
print(nums)

nums.extend(nums[:])
print(nums)

nums.insert(3, 25)
print(nums)





