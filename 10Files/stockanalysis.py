# analyse the stock prices of baidu.com: ticker symbol BIDU
total = 0.0
num = 0
fhand = open("bidu.csv")
fhand.readline()    # this discards the first line of labels
for line in fhand:
    line = line.rstrip()
    line = line.split(",")
    price = float(line[-2])
    total += price
    num += 1
average = total/num
print("average stock price: " + str(average))
