# print the city name and the pollution values for all cities
# that have a PM 10 pollution of 20 or more.
fhand = open("airpollution.txt")
for line in fhand:
    line = line.rstrip()
    line = line.split(":")
    if int(line[1]) >= 20:
        print(line[0] + "\tPM: " + line[1])



