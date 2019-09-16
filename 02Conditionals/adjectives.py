"""
The words 1st, 2nd, 3rd, 4th, etc., are called ordinal adjectives.
Write a program that assigns an integer to the variable num, and
outputs the ordinal adjective corresponding to that integer.
input: num = 1
output: 1st
"""

num = 20
if num == 1:
    print(str(num) + "st")
elif num == 2:
    print(str(num) + "nd")
elif num == 3:
    print(str(num) + "rd")
else:
    print(str(num) + "th")
