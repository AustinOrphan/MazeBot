from Sensors import Distance
from Sensors import DHT22
import RPi.GPIO as GPIO
import time
from Sensors import Light

def getLight():
    lSP = 4
    lSensor = Light.Light(lSP)
    lightR = lSensor.Measure()
    if lightR > .5:
        lightState = True
    else:
        lightState = False
    return lightState

def getTemp():
    dhtPin=2
    DHT = DHT22.DHT22(dhtPin)
    temp = DHT.getTemp()
    return temp

def getDistances():
    lDS = [12,16]
    rDS = [20,21]
    fDS = [5,6]
    distances = []
    servo(12.5)  # turn towards 90 degree
    distances.append(getDistance(fDS))
    servo(8.5)  # turn towards 0 degree
    f1=getDistance(fDS)
    servo(7.5)  # turn towards 0 degree
    f2=getDistance(fDS)
    servo(6.5)  # turn towards 0 degree
    f3=getDistance(fDS)
    distances.append((f1+f2+f3)/3)
    servo(2.5) # turn towards 180 degree
    distances.append(getDistance(fDS))
    return distances

def getFDist():
    servo(8.5)  # turn towards 0 degree
    f1=getDistance(fDS)
    servo(7.5)  # turn towards 0 degree
    f2=getDistance(fDS)
    servo(6.5)  # turn towards 0 degree
    f3=getDistance(fDS)
    return (f1+f2+f3)/3

def servo(dC):
    servoData = 14
    degrees = 0
    sleepTime = .01
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    servoData = 14
    degrees = 0
    sleepTime = .01

    GPIO.setup(servoData, GPIO.OUT)

    p = GPIO.PWM(servoData, 50)

    dutyCycle = ((degrees)/18) + 2

    p.start(7.5)

    p.ChangeDutyCycle(dC)  # turn towards 90 degree
    time.sleep(.5) # sleep 1 second
    # p.ChangeDutyCycle(7.5)  # turn towards 0 degree
    # time.sleep(1) # sleep 1 second
    # p.ChangeDutyCycle(2.5) # turn towards 180 degree
    # time.sleep(1) # sleep 1 second

def getDistance(pins):
    dS = Distance.Distance(pins[0], pins[1])
    maxInches = 500
    goodRead = False
    reads = []

    while len(reads) < 20:
        i = 0
        dS.Measure()
        read = dS.inches
        if i > 0 and read < getAvgFromList(reads) * 1.25 and read > getAvgFromList(reads) *.75:
            goodRead = True
        i += 1
        reads.append(read)

    return getAvgFromList(reads)

def getDistanceOld(pins):
    dS = Distance.Distance(pins[0], pins[1])
    maxInches = 500
    goodRead = False
    reads = []
    reads.append(maxInches)
    while not goodRead:
        dS.Measure()
        reads[0] = dS.inches
        if reads[0] < maxInches:
            goodRead = True

    iniAvg = 0
    i = 0
    while i < 5:
        dS.Measure()
        iniAvg += dS.inches
        i+=1
    iniAvg=iniAvg/i

    while len(reads) < 5:
        goodRead = False
        i = 0

        while not goodRead:
            dS.Measure()
            read = dS.inches
            i += 1
            if read < maxInches and read < getAvgFromList(reads) * 1.25 and read > getAvgFromList(reads) *.75 and i>0:
                goodRead = True
            elif read < maxInches and read < iniAvg * 1.25 and read > iniAvg * .75:
                goodRead = True

        reads.append(read)

    return getAvgFromList(reads)




def getAvgFromList(listToAvg):
    iSum = 0
    for item in listToAvg:
        iSum += item
    avg = iSum / len(listToAvg)
    return avg
