"""
The words 1st, 2nd, 3rd, etc. are called ordinal adjectives.
Write a program that assigns a variable to num between 1 and 9.
The program should output the ordinal adjective corresponding
to that number.
input: num = 1
output: 1st
"""

num = 10
if num == 1:
    print(str(num) + "st")
elif num == 2:
    print(str(num) + "nd")
elif num == 3:
    print(str(num) + "rd")
else:
    print(str(num) + "th")

