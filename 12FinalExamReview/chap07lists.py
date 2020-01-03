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

# Question 4.
nums = []
for trial in range(20):
    value = random.randint(1, 12)
    nums.append(value)
print(nums)
for i in range(len(nums)):
    value = nums[i]
    if value > 10:
        nums[i] = 10
print(nums)

# Question 5.
phrase = ["Soft", "what", "light", "through", "yonder", "window", "breaks"]
for i in range(len(phrase)):
    word = phrase[i]
    phrase[i] = word[1:]
print(phrase)

# Question 6.
nums = []
for item in range(50):
    nums.append(item)
print(nums)

nums = []
for item in range(1, 51):
    nums.append(item**2)
print(nums)

alpha = "abcdefghijklmnopqrstuvwxyz"
result = []
factor = 1
for letter in alpha:
    result.append(letter*factor)
    factor += 1
print(result)
print(factor)

# Question 7.
def columnwise(one, two):
    outcome = []
    for i in range(len(one)):
        addition = one[i] + two[i]
        outcome.append(addition)
    return outcome

result = columnwise([3, 1, 4], [1, 5, 9])
print(result)

# Question 8.
def factorize(num):
    outcome = []
    value = num//2 + 1
    for i in range(1,value):
        if num%i == 0:
            outcome.append(i)
    return outcome

result = factorize(21)
print(result)

# Question 10.
def rotatelist(nums):
    item = nums.pop(-1)
    nums.insert(0, item)
    return nums

result = rotatelist([62,79,87,98,71,94,65,41])
print(result)


# Question 11.
def separatezeros():
    outcome = [1, 1]
    for num in range(1, 11):
        outcome.extend([0]*num)
        outcome.append(1)
    return outcome

result = separatezeros()
print(result)

# Question 13.
def removerepeated(nums):
    for i in range(len(nums)-1,-1,-1):
        amount = nums.count(nums[i])
        if amount > 1:
            nums.remove(nums[i])
    return nums

result = removerepeated([1,1,2,3,1,0,1,3,4,1,0,0,1,3,0,0])
print(result)

# Question 15.
def onetimepad(plaintext):
    ciphertext = ""
    shifts = [1, 3, 2, 10, 8, 2]
    for i in range(len(plaintext)):
        code = ord(plaintext[i]) - 97
        num = (code+shifts[i])%26
        letter = chr(num+97)
        ciphertext += letter
    return ciphertext

result = onetimepad("secret")
print(result)
