# determine the number of unique countries
def destinations():
    nations = {}
    fhand = open("annualmigration.csv")
    for line in fhand:
        line = line.rstrip()
        line = line.split(",")
        place = line[1]
        nations[place] = nations.get(place, 0)
    return len(nations)

result = destinations()
print(result)

# determine a list of the origin nations
def origins(country):
    nations = []
    fhand = open("annualmigration.csv")
    for line in fhand:
        line = line.rstrip()
        line = line.split(",")
        if country == line[1] and line[2] not in nations:
            nations.append(line[2])
    nations.sort()
    return nations

result = origins("Haiti")
print(result)

# determine the largest influx during a particular year
def largestinflux(country):
    influx = {}
    fhand = open("annualmigration.csv")
    for line in fhand:
        line = line.rstrip()
        line = line.split(",")
        if country == line[1]:
            year = line[0]
            people = int(line[3])
            influx[year] = influx.get(year, 0) + people
    return max(influx.values())

result = largestinflux("United States of America")
print(result)
