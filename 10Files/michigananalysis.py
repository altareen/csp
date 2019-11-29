# determine the child poverty levels in Michigan

def highestpoverty():
    fhand = open("michigandata.txt")
    fhand.readline()
    countyname = ""
    maxrate = 0
    countpv = 0
    hhincome = 0
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        percentpv = float(line[11])
        if percentpv > maxrate:
            countyname = line[23]
            maxrate = percentpv
            countpv = int(line[8])
            hhincome = int(line[20])
    return (countyname, maxrate, countpv, hhincome)

result = highestpoverty()
print(result)
print("County name: " + result[0])
print("Percentage of children in poverty: " + str(result[1]))
print("Count of children in poverty: " + str(result[2]))
print("Median household income: " + str(result[3]))


def lowestpoverty():
    fhand = open("michigandata.txt")
    fhand.readline()
    countyname = ""
    minrate = 9999
    countpv = 0
    hhincome = 0
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        percentpv = float(line[11])
        if percentpv < minrate:
            countyname = line[23]
            minrate = percentpv
            countpv = int(line[8])
            hhincome = int(line[20])
    return (countyname, minrate, countpv, hhincome)

result = lowestpoverty()
print(result)
print("County name: " + result[0])
print("Percentage of children in poverty: " + str(result[1]))
print("Count of children in poverty: " + str(result[2]))
print("Median household income: " + str(result[3]))




def retrievedata(county):
    fhand = open("michigandata.txt")
    fhand.readline()
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        percentpv = 0.0
        countpv = 0
        hhincome = 0
        countyname = line[23]
        if county in countyname:
            percentpv = float(line[11])
            countpv = int(line[8])
            hhincome = int(line[20])
            return (countyname, percentpv, countpv, hhincome)

result = retrievedata("Wayne")
print(result)

