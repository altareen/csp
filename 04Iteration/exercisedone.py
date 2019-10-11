total = 0
num = ""
while num != "done":
    num = input("Enter a number: ")
    if num == "done":
        break
    total += int(num)
print(total)