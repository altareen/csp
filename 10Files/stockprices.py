# analysing the stock price of baidu.com, ticker symbol: BIDU
total = 0.0
num = 0
fhand = open("bidu.csv")
fhand.readline()    # discards the first line of column labels
for line in fhand:
    line = line.rstrip()
    line = line.split(",")
    price = float(line[-2])
    total += price
    num += 1
average = total/num
print("average closing price = " + str(average))
