import Adafruit_DHT

class DHT22:
    def __init__(self,pin):

        # Sensor should be set to Adafruit_DHT.DHT11,
        # Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
        self.sensor = Adafruit_DHT.DHT22

        # Example using a Raspberry Pi with DHT sensor
        # connected to GPIO23.
        self.pin = pin
        self.initLists()
        self.initVars()

    def getReading(self):
        self.initLists()
        self.initVars()
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        while len(self.hList)<5:
            h, t = Adafruit_DHT.read_retry(self.sensor, self.pin)
            self.hList.append(h)
            self.tList.append(t)
        for h in self.hList:
            self.humidity += h
        self.humidity = self.humidity/len(self.hList)
        for t in self.tList:
            self.temperature += t
        self.temperature = self.temperature/len(self.tList)


    def initLists(self):
        self.hList = []
        self.tList = []

    def initVars(self):
        self.humidity=0
        self.temperature=0


    def getTemp(self):
        self.getReading()
        return self.temperature

    def getHumi(self):
        self.getReading()
        return self.humidity

    def printReading(self):
        # Note that sometimes you won't get a reading and
        # the results will be null (because Linux can't
        # guarantee the timing of calls to read the sensor).
        # If this happens try again!
        if self.humidity is not None and self.temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(self.temperature, self.humidity))
        else:
            print('Failed to get reading. Try again!')
