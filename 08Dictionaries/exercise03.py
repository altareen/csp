# Exercise 3, page 124
emails = {}
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        line = line.split()
        address = line[1]
        if address not in emails:
            emails[address] = 1
        else:
            qty = emails[address]
            emails[address] = qty + 1
print(emails)

bigemail = ""
bignum = 0
for key in emails:
    if emails[key] > bignum:
        bigemail = key
        bignum = emails[key]
print(bigemail)
print(bignum)



