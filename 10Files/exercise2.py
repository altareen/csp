# Python for Everybody, Exercise 2, page 95
total = 0.0
qty = 0
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.split()
        num = float(line[1])
        total += num
        qty +=  1
average = total/qty
print("average = " + str(average))

