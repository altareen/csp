# Exercise 3, page 124
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    print(line)
    
