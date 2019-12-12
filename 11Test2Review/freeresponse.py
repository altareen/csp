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


# Question 4.

def validate(username, password):
    users = {"alice":"trustnoone", "bob":"burger", "carl":"basketball", "dan":"batman"}
    result = ""
    if username not in users:
        result = "invalid username"
    elif username in users and password != users[username]:
        result = "incorrect password"
    elif username in users and password == users[username]:
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
    division = {"patriots":[8,2], "bills":[7,3], "jets":[2,8], "dolphins":[1,9]}
    record = division[team]
    result = record[0]/(record[0] + record[1])
    return result

result = winpercentage("patriots")
print(result)

result = winpercentage("bills")
print(result)


def numberofwins():
    division = {"patriots": [8, 2], "bills": [7, 3], "jets": [2, 8], "dolphins": [1, 9]}
    wins = []
    for team in division:
        record = division[team]
        wins.append(record[0])
    return wins

result = numberofwins()
print(result)

















