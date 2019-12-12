# Part 3: Python Programming

# Question 1.
def inventory():
    prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}
    stock = {"banana":6, "apple":7, "orange":31, "pear":15}
    total = 0.0
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
    if 0 <= value <= 10:
        result = nums[eng]
    elif 11 <= value <= 19:
        digit = eng[1]
        result = "shi " + nums[digit]
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


# Question 4.

def validate(username, password):
    credentials = {"alice":"trustnoone", "bob":"burger", "carl":"baskeball"}
    result = ""
    if username not in credentials:
        result = "invalid username"
    elif username in credentials and password != credentials[username]:
        result = "incorrect password"
    elif username in credentials and password == credentials[username]:
        result = "login successful"
    return result

result = validate("jim", "football")
print(result)

result = validate("bob", "pizza")
print(result)

result = validate("alice", "trustnoone")
print(result)


# Question 5.

def winpercentage(team):
    division = {"patriots":[8,2], "bills":[7,3], "jets":[4,6], "dolphins":[1,9]}
    record = division[team]
    result = record[0]/(record[0] + record[1])
    return result

result = winpercentage("patriots")
print(result)

result = winpercentage("bills")
print(result)

def numberofwins():
    division = {"patriots": [8, 2], "bills": [7, 3], "jets": [4, 6], "dolphins": [1, 9]}
    wins = []
    for team in division:
        record = division[team]
        wins.append(record[0])
    return wins

result = numberofwins()
print(result)

# Question 34.

def listintersection(first, second):
    result = []
    for num in first:
        if num in second:
            result.append(num)
    return result

result = listintersection([1, 3, 5], [5, 3])
print(result)

result = listintersection([2,3,8,9,4,12,8,13,19,7,6], [1,9,3,8,4,7,9,13])
print(result)

# Question 35.

def middle(nums):
    size = len(nums)
    center = size//2
    return nums[center]

result = middle([8, 0, 100, 12, 1])
print(result)











