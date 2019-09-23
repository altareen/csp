def computegrade(score):
    grade = ""
    if type(score) == str or score < 0 or score > 1.0:
        grade = "Bad score"
    elif score > 0.9:
        grade = "A"
    elif score > 0.8:
        grade = "B"
    elif score > 0.7:
        grade = "C"
    elif score > 0.6:
        grade = "D"
    else:
        grade = "F"
    return grade

result = computegrade(0.9)
print("Grade: " + result)
