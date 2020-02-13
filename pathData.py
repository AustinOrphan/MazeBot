import os

class robotData:
    def __init__(self, timeTravelled, powerUsed, detectedDistances, temp, light):
        self.data = [timeTravelled, powerUsed, detectedDistances, temp, light]

dataList = []
dataList.append(data)

def writePathData(timeTravelled, powerUsed, detectedDistances, temp, light):
    wFile = os.open("pathData.csv","w")

    for datum in data:
        wFile.write(datum, ",")
    os.close(wFile)
