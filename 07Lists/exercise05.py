# Exercise 5: Determine a count of email sender addresses
count = 0
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        line = line.split()
        print(line[1])
        count += 1
print("Number of email addresses: " + str(count))

# determine the intersection of two lists
def intersection(first, second):
    result = []
    for num in first:
        if num in second:
            result.append(num)
    return result

outcome = intersection([1,3,5], [5,3,1])
print(outcome)
outcome = intersection([1,3,6,9], [10,14,3,72,9])
print(outcome)
outcome = intersection([2,3], [3,3,3,2,10])
print(outcome)
outcome = intersection([2,4,6], [1,3,5])
print(outcome)

# determine the smallest positive integer not in the list
def nextnumber(nums):
    if len(nums) == 0:
        return 1
    largest = max(nums)
    for item in range(1, largest+1):
        if item not in nums:
            return item
    return 1

solution = nextnumber([5,3,1])
print(solution)
solution = nextnumber([5,4,1,2])
print(solution)
solution = nextnumber([2,3])
print(solution)
solution = nextnumber([])
print(solution)




