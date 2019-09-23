def computepay(hours, rate):
    pay = 0
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * (rate * 1.5)
    return pay

result = computepay(50, 10)
print("Pay: " + str(result))
