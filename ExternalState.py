from Sensors import Distance
from Sensors import DHT22
from Sensors import Light

def getLight():
    lSP = 4
    lSensor = Light.Light(lSP)
    lSensor.Measure()

def getDistances():
    lDS = [12,16]
    rDS = [20,21]
    fDS = [5,6]
    distances = []
    distances.append(getDistance(lDS))
    distances.append(getDistance(fDS))
    distances.append(getDistance(rDS))
    return distances

def getDistance(pins):
    dS = Distance.Distance(pins[0], pins[1])
    maxInches = 160
    goodRead = False
    reads = []
    reads.append(maxInches)
    while not goodRead:
        dS.Measure()
        reads[0] = dS.inches
        if reads[0] < maxInches:
            goodRead = True


    while len(reads) < 5:
        goodRead = False
        i = 0

        while not goodRead:
            dS.Measure()
            read = dS.inches
            i += 1
            if read < maxInches and read < getAvgFromList(reads) * 1.25 and read > getAvgFromList(reads) *.75:
                goodRead = True

        reads.append(read)

    return getAvgFromList(reads)




def getAvgFromList(listToAvg):
    iSum = 0
    for item in listToAvg:
        iSum += item
    avg = iSum / len(listToAvg)
    return avg
