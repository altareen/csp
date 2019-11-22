# open the file mailbox.txt in read mode
fhand = open("mailbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

# open the file datadump.txt in write mode
fout = open("datadump.txt", "w")
fout.write("Here is the lunch menu.\n")
food = "pizza, burgers, soda\n"
fout.write(food)
fout.close()

