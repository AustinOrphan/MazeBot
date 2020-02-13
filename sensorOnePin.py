class Distance:
    def __init__(self, pin):
        self.pin = pin

    def Measure(self):
        import RPi.GPIO as GPIO
        import time
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        pin = self.pin

        print "Distance Measurement in Progress"

        # GPIO.setup(pin,GPIO.OUT)
        # GPIO.setup(pin,GPIO.IN)



        pulse_start = -1
        pulse_end = -1

        while pulse_start == -1 or pulse_end == -1:
            pulse_start = -1
            pulse_end = -1
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, False)
            print "Waiting for Sensor to Settle"
            time.sleep(.0001)
            print "Before pulse_start"
            GPIO.output(pin, True)
            time.sleep(0.00001)
            GPIO.output(pin, False)

            GPIO.setup(pin,GPIO.IN)
            while GPIO.input(pin)==0:
                pulse_start = time.time()

            while GPIO.input(pin)==1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        centimeters = pulse_duration * 17150
        inches = centimeters * 0.393701

        self.centimeters = round(centimeters, 2)
        print "Distance in centimeters: ", centimeters, "cm"

        inches = round(inches, 2)
        print "Distance in inches: ", inches, "in"

        GPIO.cleanup()
        self.inches = inches

distance1 = Distance(6)
# distance2 = Distance(21,20)
# distance3 = Distance(12,16)
distance1.Measure()
# distance2.Measure()
# distance3.Measure()
print distance1.inches
# print distance2.inches
# print distance3.inches
