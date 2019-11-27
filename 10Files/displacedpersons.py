# determine the number of unique countries
def destinations():
    countries = {}
    fhand = open("annualmigration.csv")
    for line in fhand:
        line = line.rstrip()
        line = line.split(",")
        nation = line[1]
        countries[nation] = countries.get(nation, 0)
    return len(countries)
result = destinations()
print(result)

def origins(country):
    nations = []
    fhand = open("annualmigration.csv")
    for line in fhand:
        line = line.rstrip()
        line = line.split(",")
        if line[1] == country and line[2] not in nations:
            nations.append(line[2])
    nations.sort()
    return nations

result = origins("Haiti")
print(result)


def largestinflux(country):
    influx = {}
    fhand = open("annualmigration.csv")
    for line in fhand:
        line = line.rstrip()
        line = line.split(",")
        if line[1] == country:
            influx[line[0]] = influx.get(line[0], 0) + int(line[3])
    return max(influx.values())

result = largestinflux("United States of America")
print(result)












