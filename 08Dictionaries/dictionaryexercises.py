# Python for Everybody, Exercise 5, page 124
institutions = {}
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        line = line.split()
        address = line[1]
        pos = address.find("@")
        domain = address[pos+1:]
        if domain not in institutions:
            institutions[domain] = 1
        else:
            qty = institutions[domain]
            institutions[domain] = qty + 1
print(institutions)

# Introduction to Python, Exercise 4, page 105
def validate(username, password):
    outcome = ""
    credentials = {"alice":"trustnoone", "bob":"basketball", "carl":"ilikepizza", "dan":"batman"}
    if username not in credentials:
        outcome = "username not valid."
    elif username in credentials and credentials[username] != password:
        outcome = "incorrect password."
    elif username in credentials and credentials[username] == password:
        outcome = "user is logged in."
    return outcome

result = validate("edward", "hamburgers")
print(result)

result = validate("bob", "football")
print(result)

result = validate("alice", "trustnoone")
print(result)

# Introduction to Python, Exercise 5, page 105
def winpercentage(name):
    football = {"patriots":[8, 2], "bills":[6, 3], "jets":[2, 7], "dolphins":[2, 7]}
    record = football[name]
    outcome = record[0]/(record[0] + record[1])
    return outcome

result = winpercentage("patriots")
print(result)

def numberofwins():
    football = {"patriots": [8, 1], "bills": [6, 3], "jets": [2, 7], "dolphins": [2, 7]}
    result = []
    for key in football:
        record = football[key]
        result.append(record[0])
    return result

wins = numberofwins()
print(wins)

def winningrecords():
    football = {"patriots": [8, 1], "bills": [6, 3], "jets": [2, 7], "dolphins": [2, 7]}
    outcome = []
    for key in football:
        if winpercentage(key) >= 0.5:
            outcome.append(key)
    return outcome

result = winningrecords()
print(result)








