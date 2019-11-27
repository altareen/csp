# determine the average intensity of solar activity
# over a particular time range of years/months.
annualsun = {}

def initialize(filename, sundict):
    fhand = open(filename)
    fhand.readline()
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        #print(line)
        intensity = []
        for i in range(1, len(line)):
            intensity.append(float(line[i]))
        #print(intensity)
        year = int(line[0])
        sundict[year] = intensity

def averagesolar(sundict, years, months):
    total = 0.0
    num = 0
    realm = list(range(years[0], years[1]+1))
#    print(realm)
    domain = list(range(months[0]-1, months[1]))
#    print(domain)
    for year in realm:
        intensity = sundict[year]
        for month in domain:
#            print(intensity[month])
            total += intensity[month]
            num += 1
    return total/num

initialize("solardata.txt", annualsun)
#print(annualsun)


result = averagesolar(annualsun, (1900, 1905), (1, 1))
print("Average solar intensity:", result)

result = averagesolar(annualsun, (2000, 2010), (1, 6))
print("Average solar intensity:", result)

result = averagesolar(annualsun, (1749, 2010), (1, 1))
print("Average solar intensity:", result)

result = averagesolar(annualsun, (1900, 1905), (1, 12))
print("Average solar intensity:", result)
