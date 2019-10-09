total = 0
num = ""
while num != "done":
    num = input("Enter a number: ")
    if num != "done":
        total += int(num)
print("Total: " + str(total))
