# Determine the largest, smallest and average PM10/PM2.5 values
largest25 = 0
city25 = ""
lowest25 = 9999
lowestcity = ""
total = 0
num = 0
fhand = open("airpollution.txt")
for line in fhand:
    line = line.rstrip()
    line = line.split(":")
    if int(line[2]) > largest25:
        largest25 = int(line[2])
        city25 = line[0]
    if int(line[2]) < lowest25:
        lowest25 = int(line[2])
        lowestcity = line[0]
    total += int(line[2])
    num += 1

print("City with largest PM2.5: " + city25 + " PM2.5: " + str(largest25))
print("City with lowest PM2.5: " + lowestcity + " PM2.5: " + str(lowest25))
print("Average PM2.5: " + str(total/num))
