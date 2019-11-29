# determine the highest percentage of children in poverty

def highestpoverty():
    fhand = open("michigandata.txt")
    fhand.readline()
    largest = 0
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        percent = float(line[11])
        if percent > largest:
            quantity = int(line[8])
            largest = percent
            income = int(line[20])
            county = line[23]
    return (county, income, largest, quantity)

result = highestpoverty()
print(result)


def lowestpoverty():
    fhand = open("michigandata.txt")
    fhand.readline()
    lowest = 100.0
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        percent = float(line[11])
        if percent < lowest:
            quantity = int(line[8])
            lowest = percent
            income = int(line[20])
            county = line[23]
    return (county, income, lowest, quantity)

result = lowestpoverty()
print(result)



def retrievedata(name):
    fhand = open("michigandata.txt")
    fhand.readline()
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        county = line[23]
        if name in county:
            quantity = int(line[8])
            percent = float(line[11])
            income = int(line[20])
            return (county, income, percent, quantity)

result = retrievedata("Wayne")
print(result)







